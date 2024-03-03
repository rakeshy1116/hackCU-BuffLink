from flask import Flask, request 
 
app = Flask(__name__)   
 

@app.route('/', methods =["POST"])
def gfg():
    

    data = request.get_json()
    print(data)
    return data
    
 
if __name__=='__main__':
   app.run()