# encoding=utf-8

import json
from local_settings import *
from slackclient import SlackClient
from flask import Flask, request, make_response

app = Flask(__name__)
client = SlackClient(BOT_TOKEN)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/events', methods=["GET", "POST"])
def respond_to_event():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
    else:
        print request.json
        client.api_call('chat.postMessage', channel=request.json['event']['channel'], text="Hi There!", icon_emoji=":grinning:")
        return make_response("Gotcha", 200)


if __name__ == '__main__':
    app.run()
