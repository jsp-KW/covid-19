import os

TELEGRAM_TOKEN = os.envrion.get('TELEGRAM_TOKEN','')
CHAT_ID = os.environ.get('CHAT_ID','')


if not TELEGRAM_TOKEN or not CHAT_ID:
    raise Exception ('TELEGRAM_TOKEN, CHAT_ID 확인 필요')