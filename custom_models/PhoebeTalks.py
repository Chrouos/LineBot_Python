from __future__ import unicode_literals
import os

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, PostbackEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage

import configparser

import random

# 我們的函數
from custom_models import utils

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))


# 找尋關鍵字
def keyword_reply(event):
    
    if '你好'in event.message.text:
        
        try:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage('不過，如果有問題歡迎到 https://www.pccu.edu.tw/ 搜尋')
            )

        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='失敗了')
            )

        return True
    else:
        return False


# 重複說話
def echo(event):
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

    return True

