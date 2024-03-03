from flask import Flask, request 
from flask_cors import CORS
from user_dynamo import *
 
app = Flask(__name__)   
CORS(app, resources={r"/*": {"origins": "*"}})
 

@app.route('/', methods =["POST"])
def gfg():
    data = request.get_json()
    print(data)
    # print(data['email'])
    user_data = get_user_data(data['email'])
    # change this list of textprompts
    empty_list = []
    empty_list.append(data['text'])

    if user_data is not None:
        print("User data:", user_data)
        stringList = user_data.get('previousMails', {}).get('L', [])
        put_user_data(data['name'], data['email'], stringList, empty_list)
    else:
        put_user_data(data['name'], data['email'], [], empty_list) 
    return data
    
 
if __name__=='__main__':
   app.run(debug=True, port=5002)