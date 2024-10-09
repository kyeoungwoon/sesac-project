import requests
import json

# config.json 파일 경로
config_file = 'telegram-bot/config.json'

# JSON 파일 불러오기
with open(config_file, 'r') as file:
    config = json.load(file)

# JSON 데이터에서 필요한 값들 가져오기
TELEGRAM_BOT_TOKEN = config.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = config.get('CHAT_ID_KYEOUNG_WOON')
WEBHOOK_URL = config.get('WEBHOOK_URL')

def send_message(message):
    # 텔레그램 API URL
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    response = requests.post(url, data={'chat_id': CHAT_ID, 'text': message})
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print('Failed to send message.')

print(TELEGRAM_BOT_TOKEN)