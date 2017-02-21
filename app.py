from flask import Flask, request
import json
import requests,os
 
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    print("user: ",user)
    sendText(user,'what?') #send message
    return '',200  
def sendText(user, text):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'LQINTwiRBOztCajzLlm+v2uTDkiYtOdw790W5gItxLukx1L9InomCUKdMe1NgVB7jqzxOam4uiqLhY2SveEXIEKKKtW4W53u/WLBb65EAwAHHJzFwYEVZ0v76xHwosiSfrAis5Ih6iJnCdy/DlJDXwdB04t89/1O/w1cDnyilFU='
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }
    data = json.dumps({
        "replyToken":user,
        "messages":[{
            "type":"text",
            "text":text
        }]
    })
    r = requests.post(LINE_API, headers=headers, data=data)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
