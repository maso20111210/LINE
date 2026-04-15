import os
from linebot import LineBotApi
from linebot.models import TextSendMessage

# 這裡會自動抓取之後設定在 Secrets 的資料
token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
user_id = os.getenv('LINE_USER_ID')

def send_message():
    line_bot_api = LineBotApi(token)
    try:
        # 提醒文字可以自己改
        line_bot_api.push_message(user_id, TextSendMessage(text='💊 該吃鐵劑囉！'))
        print("提醒已成功發送！")
    except Exception as e:
        print(f"發送失敗，錯誤原因: {e}")

if __name__ == "__main__":
    send_message()
