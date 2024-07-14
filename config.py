import os

# قراءة القيم من متغيرات البيئة
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# قراءة القنوات المطلوبة كقائمة من متغير البيئة وتحويلها إلى قائمة باستخدام split(',')
REQUIRED_CHANNELS = os.getenv('REQUIRED_CHANNELS').split(',')

# قراءة معرف المطور
DEVELOPER_ID = int(os.getenv('DEVELOPER_ID'))
