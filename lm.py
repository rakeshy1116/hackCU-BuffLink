import torch
from transformers import BartForSequenceClassification, BartTokenizer

tokenizer = BartTokenizer.from_pretrained('valhalla/distilbart-mnli-12-1')
model = BartForSequenceClassification.from_pretrained('valhalla/distilbart-mnli-12-1')

def check_relevancy(event_desc, topics):

    premise_batched = [event_desc] * len(topics)

    input_ids = tokenizer(premise_batched, topics, return_tensors="pt", padding=True)

    logits = model(input_ids['input_ids'])['logits']

    entail_contradiction_logits = logits[:, [0, 2]]
    probs = entail_contradiction_logits.softmax(dim=1)
    
    true_probs = probs[:, 1] * 100
    true_probs = true_probs.tolist()

    for val in true_probs:
        if val > 60:
            return True
        
    return False

    
