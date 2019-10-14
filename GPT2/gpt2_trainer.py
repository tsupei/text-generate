from transformers import (WEIGHTS_NAME, AdamW, WarmupLinearSchedule,
                          GPT2Config, GPT2LMHeadModel, GPT2Tokenizer,
                          OpenAIGPTConfig, OpenAIGPTLMHeadModel, OpenAIGPTTokenizer)
from generic import GenericTrainer, GenericDataset


class GPT2Trainer(GenericTrainer):
    def __init__(self):
        super().__init__()
        pass
    
    def train_model(self):
        pass
    
    def test_model(self):
        pass
    
    def predict(self):
        pass

