from transformers import AutoModelForCausalLM, AutoTokenizer
from torch.nn import DataParallel
from flask import Flask, jsonify, request, render_template
from os.path import dirname

# Load the model and tokenizer
model_path = "./MJ-prompts/checkpoint-63/"  # Replace with the actual path to your model
model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)

def get_mj(text):

    input_text = f'''
    ###Human:
    generate a midjourney prompt for {text}

    ### Assistant:
    '''

    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text using the model
    output = model.generate(input_ids, max_length=85, num_return_sequences=1,do_sample=True)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    print(generated_text)
    return generated_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    text_param = request.args.get('text')
    res = get_mj(text_param)
    print("res",res)
    data = {'Result': res}
    return jsonify(data)



if __name__ == '__main__':
    #loadPDF()
    app.run(host='0.0.0.0',debug=False, port=3001)
