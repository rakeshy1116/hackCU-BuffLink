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

    for topic in topics:
        input_ids = tokenizer(event_desc, topic, return_tensors="pt", padding=True)

        logits = model(input_ids['input_ids'])['logits']

        entail_contradiction_logits = logits[:, [0, 2]]
        probs = entail_contradiction_logits.softmax(dim=1)
    
        true_probs = probs[:, 1] * 100
        true_probs = true_probs.tolist()
        #
        for val in true_probs:
            if val > 75:
                return True
        
    return False

    

app = Flask(__name__)   
CORS(app, resources={r"/*": {"origins": "*"}})
 

@app.route('/', methods =["POST"])
def gfg():
    data = request.get_json()
    print("User Data (Json):")
    print(data)
    print(' ')
    user_data = get_user_data(data['email'])
    extensionPrompts = []
    text_list = json.loads(data['text'])
    
    for i in text_list:
        # print(i)
        extensionPrompts.append(i)
  
    if user_data is not None:
        stringList = user_data.get('previousMails', {}).get('L', [])
        stringList_list = [item.get('S') for item in stringList]
        # print(stringList)
        put_user_data(data['name'], data['email'], stringList_list, extensionPrompts)
    else:
        put_user_data(data['name'], data['email'], [], extensionPrompts) 

    print("Updated User preferences in database for future communications.")
    print(' ')
    for i in range(len(extensionPrompts)):
        extensionPrompts[i] = 'This text is about or relavant to ' + extensionPrompts[i] + '.'
    all_events = get_events_dynamo()
    possible_events = []
    print('Bart LLM is finding relevant events for the user: ' + data['name'])
    print(' ')
    for item in all_events:
        relevant = check_relevancy(item.get('title').get('S')+ ' ' + item.get('description').get('S'), extensionPrompts)
        if(relevant):
            print(item.get('title').get('S') + ' event '+ 'is relevant to user preference')
            print(' ')
            possible_events.append(item.get('hash_id').get('S') )

    print('Mailing the relevant events to: ' + data['email'])
    print(' ')
    email_handler(data['email'],possible_events)

    return data
    
 
if __name__=='__main__':
   app.run(debug=True, port=5007)