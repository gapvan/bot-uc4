# -*- coding: utf-8 -*-
from flask import Flask, request
import json
import requests
 
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World!"

#callback Webhook
@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    #id=[d['replyToken'] for d in user][0]
    #print(json_line)
    print("user：",user)
    sendText(user,'what?') #send message
    return '',200
 
def sendText(user, text):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer ENTER_ACCESS_TOKEN'
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
     app.run(debug=True)
