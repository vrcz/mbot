import os

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# أضف معرفات القنوات المطلوبة هنا
REQUIRED_CHANNELS = os.getenv('REQUIRED_CHANNELS').split(',')
DEVELOPER_ID = int(os.getenv('DEVELOPER_ID'))
