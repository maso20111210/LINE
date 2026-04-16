import os
import random
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage

token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
user_id = os.getenv('LINE_USER_ID')

def send_message():
    line_bot_api = LineBotApi(token)
    
    images = [
        "https://github.com/maso20111210/20111210/blob/main/01.png?raw=true",
        "https://github.com/maso20111210/20111210/blob/main/02.png?raw=true",
        "https://github.com/maso20111210/20111210/blob/main/03.png?raw=true",
        "https://github.com/maso20111210/20111210/blob/main/04.png?raw=true",
        "https://github.com/maso20111210/20111210/blob/main/05.png?raw=true",
        "https://github.com/maso20111210/20111210/blob/main/06.png?raw=true",
        "https://github.com/maso20111210/20111210/blob/main/07.png?raw=true",
        "https://github.com/maso20111210/20111210/blob/main/08.png?raw=true"
    ]
    
    texts = ["💊 該吃鐵劑囉！", "💊 記得吃藥喔！", "💊 補鐵時間到了！","💊 該吃鐵劑囉！配點柳橙汁（維他命C）吸收效果更好喔。","💊 補鐵時間到！記得這一個小時內先不要喝茶或咖啡，以免影響吸收。","💊 該補鐵了，建議空腹服用效果最棒喔！","💊 忙碌之餘也別忘了照顧身體，快把鐵劑吃下去吧！","💊 叮咚！吃鐵劑的時間準時報到。"]

    img_url = random.choice(images)
    msg_text = random.choice(texts)

    try:
        line_bot_api.push_message(
            user_id,
            [
                ImageSendMessage(original_content_url=img_url, preview_image_url=img_url),
                TextSendMessage(text=msg_text)
            ]
        )
        print("提醒已成功發送！")
    except Exception as e:
        print(f"發送失敗: {e}")

if __name__ == "__main__":
    send_message()
