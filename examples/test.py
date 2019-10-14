import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

input_ids = torch.tensor(tokenizer.encode("America is known as a")).unsqueeze(0)
outputs = model(input_ids, labels=input_ids)
loss, logits = outputs[:2]


print(loss, logits)

