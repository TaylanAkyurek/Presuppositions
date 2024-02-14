#
import transformers

print(transformers.__version__)

from datasets import load_dataset

datasets = load_dataset("text", data_files={"train": "big-presBelowSentenceTwo.txt", "validation": "testData.txt"})

from datasets import ClassLabel
import random
import pandas as pd
from IPython.display import display, HTML

def show_random_elements(dataset, num_examples=10):
    assert num_examples <= len(dataset), "Can't pick more elements than there are in the dataset."
    picks = []
    for _ in range(num_examples):
        pick = random.randint(0, len(dataset)-1)
        while pick in picks:
            pick = random.randint(0, len(dataset)-1)
        picks.append(pick)

    df = pd.DataFrame(dataset[picks])
    for column, typ in dataset.features.items():
        if isinstance(typ, ClassLabel):
            df[column] = df[column].transform(lambda i: typ.names[i])
    display(HTML(df.to_html()))

show_random_elements(datasets["train"])

model_checkpoint = "distilgpt2"

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)

def tokenize_function(examples):
    return tokenizer(examples["text"])

tokenized_datasets = datasets.map(tokenize_function, batched=True, num_proc=4, remove_columns=["text"])

tokenized_datasets["train"][1]

# block_size = tokenizer.model_max_length
block_size = 128

def group_texts(examples):
    # Concatenate all texts.
    concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    total_length = len(concatenated_examples[list(examples.keys())[0]])
    # We drop the small remainder, we could add padding if the model supported it instead of this drop, you can
        # customize this part to your needs.
    total_length = (total_length // block_size) * block_size
    # Split by chunks of max_len.
    result = {
        k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
        for k, t in concatenated_examples.items()
    }
    result["labels"] = result["input_ids"].copy()
    return result

lm_datasets = tokenized_datasets.map(
    group_texts,
    batched=True,
    batch_size=1000,
    num_proc=4,
)

tokenizer.decode(lm_datasets["train"][1]["input_ids"])

from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(model_checkpoint)

from transformers import Trainer, TrainingArguments

model_name = model_checkpoint.split("/")[-1]
training_args = TrainingArguments(
    f"{model_name}-finetuned-eli5",
    evaluation_strategy = "epoch",
    learning_rate=2e-5,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=lm_datasets["train"],
    eval_dataset=lm_datasets["validation"],
)

trainer.train()

import math
eval_results = trainer.evaluate()
print(f"Perplexity: {math.exp(eval_results['eval_loss']):.2f}")

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from bert_score import score

tokenizer = AutoTokenizer.from_pretrained('distilgpt2')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

test_data = []

with open('testData.txt', 'r', encoding='utf-8') as file:
    test_data = [line.strip() for line in file if line.strip()]

predictions = []
refs = []

# Function to split string at the middle but not cut a word into half
def split_string(s):
    if ' ' not in s:  # If the text doesn't contain a space, return the text as is
        return s, ''
    else:
        midpoint = len(s) // 2  # Integer division to get the middle index
        while midpoint < len(s) - 1 and s[midpoint] != ' ':
            midpoint += 1
        return s[:midpoint], s[midpoint:]

i = 0
# Generate predictions
for line in test_data[:200]:
    prompt, expected_completion = split_string(line)
    inputs = tokenizer.encode(prompt, return_tensors='pt').to(device)
    outputs = model.generate(inputs, max_length=250, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    generated_completion = tokenizer.decode(outputs[0])[len(tokenizer.decode(inputs[0])):]
    print(generated_completion.strip())
    print(expected_completion.strip())
    predictions.append(generated_completion.strip())
    refs.append(expected_completion.strip())
    print(i)
    i = i + 1


P, R, F1 = score(predictions, refs, lang='en', model_type='bert-base-uncased')

print(f"Mean F1 BERTScore: {F1.mean().item()}")

