# midjourney-chat-bot

create a dataset for creating a prompt given a concept.
Use  Llama-2 7B model using the HuggingFace auto train-advanced package.


1. Training dataset

   train.csv created for midjourney promts

2. train model

   Run the bellow command from the dataset folder  

   autotrain llm --train --project_name 'MJ-prompts' --model 'abhishek/llama-2-7b-hf-small-shards' --data_path . --use_peft --use_int4 --learning_rate 2e-4 --train_batch_size 4 --num_train_epochs 9 --trainer sft  > training.logs


3. Start API

   python3 app.py

   link : http://localhost:3001/

4. Implementation Demo link- 

   link: http://122.169.118.18:3001/

5. midjourney Example :  
   1. "Arizona Desert Sunset"
   2. "Mumbai skyline with sea"
   3. "Rural Village Cricket Match"
   4. "Kruger National Park's Wildlife"

6. youtube video link : https://www.youtube.com/watch?v=gZhCbkrT2x8
