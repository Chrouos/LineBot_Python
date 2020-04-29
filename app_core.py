from __future__ import unicode_literals
import os
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

from custom_models import utils, PhoebeTalks

app = Flask(__name__)


# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

@app.route("/")
def home():
    return render_template("home.html")

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def reply_text_message(event):
    
    # Success 200 不可刪除
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

    	reply = False

    	if not reply:
    		#找尋關鍵字
    		reply = PhoebeTalks.keyword_reply(event)
    	if not reply:
    		#重複說話
    		reply = PhoebeTalks.echo(event)




if __name__ == "__main__":
    app.run()


    