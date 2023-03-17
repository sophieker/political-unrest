import torch 
import torch.nn as nn
import torch.nn.functional as F

import transformers
from transformers import RobertaModel, RobertaConfig
from transformers import RobertaTokenizer, RobertaForSequenceClassification

import numpy as np 

tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
roberta = RobertaModel.from_pretrained('roberta-base', return_dict = False)

class roberta_arch(nn.Module):

    def __init__(self, roberta_model):
        super(roberta_arch, self).__init__()
        self.roberta = roberta_model
        self.dropout = nn.Dropout(0.1)
        self.fc1 = nn.Linear(768, 64)
        self.classifier = nn.Linear(64, 1)

    def forward(self, input_ids, attention_mask):
        _, pooled_output = self.roberta(input_ids=input_ids, attention_mask=attention_mask)
        output = self.dropout(pooled_output)
        output = self.fc1(output)
        output = self.classifier(output)
        output = torch.sigmoid(output)
        return output

model = roberta_arch(roberta)

