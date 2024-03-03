from flask import Flask, request 
from flask_cors import CORS
from user_dynamo import *
import json
import torch
from transformers import BartForSequenceClassification, BartTokenizer
from events_tableget import *
from email_handler import *

tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-mnli')
model = BartForSequenceClassification.from_pretrained('facebook/bart-large-mnli')

def check_relevancy(event_desc, topics):

    premise_batched = [event_desc] * len(topics)

    print(event_desc)
    print(topics)
    for topic in topics:
        input_ids = tokenizer(event_desc, topic, return_tensors="pt", padding=True)

        logits = model(input_ids['input_ids'])['logits']

        entail_contradiction_logits = logits[:, [0, 2]]
        probs = entail_contradiction_logits.softmax(dim=1)
    
        true_probs = probs[:, 1] * 100
        true_probs = true_probs.tolist()
        print(true_probs)
        for val in true_probs:
            if val > 75:
                return True
        
    return False

    

app = Flask(__name__)   
CORS(app, resources={r"/*": {"origins": "*"}})
 

@app.route('/', methods =["POST"])
def gfg():
    data = request.get_json()
    print(data)
    user_data = get_user_data(data['email'])
    extensionPrompts = []
    text_list = json.loads(data['text'])
    
    for i in text_list:
        # print(i)
        extensionPrompts.append(i)
  
    if user_data is not None:
        stringList = user_data.get('previousMails', {}).get('L', [])
        stringList_list = [item.get('S') for item in stringList]
        print(stringList)
        put_user_data(data['name'], data['email'], stringList_list, extensionPrompts)
    else:
        put_user_data(data['name'], data['email'], [], extensionPrompts) 

    for i in range(len(extensionPrompts)):
        extensionPrompts[i] = 'This text is about or relavant to ' + extensionPrompts[i] + '.'
    all_events = get_events_dynamo()
    possible_events = []
    for item in all_events:
        
        # print(item.get('description'))
        # print(item.get('title'))
        # print(item.get('hash_id'))
    # event = ''' Understand what mental health looks like at CU, how to recognize signs of distress, and how to connect students with available campus resources. Attending this session will help prepare you to act when you are needed most'''
        
    # for i in extensionPrompts:
    #     print(i)
        relevant = check_relevancy(item.get('title').get('S')+ ' ' + item.get('description').get('S'), extensionPrompts)
        if(relevant):
            possible_events.append(item.get('hash_id').get('S'))
        print(possible_events)

    email_handler(data['email'],possible_events)

    return data
    
 
if __name__=='__main__':
   app.run(debug=True, port=5003)