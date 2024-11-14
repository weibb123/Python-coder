# Python-coder
Finetune Python code dataset from Huggingface with Unsloth.AI via QLora Technique with Tesla T4 GPU. Free colab notebook!!

## Description
Fine-tuned the Llama 3.2-1B model using the QLoRA technique on 143,327 Python examples sourced from Hugging Face, leveraging Unsloth.AI to achieve specialized expertise in Python query handling

Built a production-ready FastAPI service integrated with LangChain to manage and return Python code-related queries, improving response precision and reliability

```git clone https://github.com/weibb123/Python-coder.git```

```pip install requirements.txt```, dont forget to create a virtual environment!

## Whole Story
Got a few minutes to read about LLM? Here is the blog post I wrote on Medium!! [Blog_to_update]()

## Finetuning
The notebook to finetune llama3.2-1b is located in finetuning. Modify notebook from Unsloth.AI tutorial to fit custom dataset.

The dataset to finetune llama3.2-1b can be found from huggingface: [dataset](https://huggingface.co/datasets/Vezora/Tested-143k-Python-Alpaca)

You can also find the finetuned model at my huggingface space [huggingface](https://huggingface.co/weibb)

![image](https://github.com/user-attachments/assets/592265f7-6f1a-495d-9414-2fa728aa598b)

It comes with various gguf, Q4_K_M, Q5_K_M, Q8_0

## FastAPI

```fastapi dev main.py``` for development

navaigate

```API docs: http://127.0.0.1:8000/docs``` to try out the query

Simply modify your questions!
![image](https://github.com/user-attachments/assets/44dd27c0-1ce4-44bb-a961-d7c309d848d6)

**Response**
![image](https://github.com/user-attachments/assets/7eedb5ff-0896-4693-9a8b-28af0bab58be)


You can also experiment it with langchain in **test.ipynb** for notebook playground style, for data folks.


## Ollama Usage

```ollama run hf.co/weibb/model:Q4_K_M```

