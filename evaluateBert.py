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

print(len(hyps))
print(len(predictions))
print(len(refs))
# Calculate BERTScore
hyps = [pred for pred in predictions if pred]

P, R, F1 = score(predictions, refs, lang='en', model_type='bert-base-uncased')

print(f"Mean F1 BERTScore: {F1.mean().item()}")
