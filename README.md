# Python-coder
Finetune Python code dataset from Huggingface with Unsloth.AI via QLora Technique with T4 GPU

## Finetuning
The notebook to finetune llama3.2-1b is located in finetuning. Modify notebook from Unsloth.AI tutorial to fit custom dataset.

The dataset to finetune llama3.2-1b can be found from huggingface: 

You can also find the finetuned model at my huggingface space [huggingface](https://huggingface.co/weibb)

![image](https://github.com/user-attachments/assets/592265f7-6f1a-495d-9414-2fa728aa598b)

It comes with various gguf, Q4_K_M, Q5_K_M, Q8_0

## FastAPI

```fastapi dev main.py``` for development

navaigate

```API docs: http://127.0.0.1:8000/docs``` to try out the query

Simply modify your questions!
![image](https://github.com/user-attachments/assets/44dd27c0-1ce4-44bb-a961-d7c309d848d6)

You can also experiment it in **test.ipynb**


## Ollama Usage

```ollama run hf.co/weibb/model:Q4_K_M```

