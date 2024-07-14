import os
from telethon import TelegramClient, events
import yt_dlp
import re
import asyncio

from config import API_ID, API_HASH, BOT_TOKEN, REQUIRED_CHANNELS
from stats import format_statistics, DEVELOPER_ID
from database import add_user, add_message, get_statistics

# إنشاء عميل Telegram
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# دالة لتحميل الفيديو
def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded_video.%(ext)s',  # اسم ملف ثابت لتجنب مشكلة طول الاسم
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            video_info = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(video_info)
            return filename
        except Exception as e:
            print(f"Error downloading video: {e}")
            return None

# دالة للتحقق من الاشتراك في القنوات المطلوبة
async def check_subscription(user_id):
    for channel in REQUIRED_CHANNELS:
        try:
            participant = await client.get_participant(channel, user_id)
            if participant.participant.left:
                return False
        except:
            return False
    return True

# حدث لمعالجة الأوامر
@client.on(events.NewMessage)
async def handler(event):
    user_id = event.sender_id
    chat_id = event.chat_id
    men = f"[{event.sender.first_name}](tg://user?id={user_id})"
    
    # سجل المستخدم والرسالة
    add_user(user_id)
    add_message(user_id, chat_id)
    
    # تحقق مما إذا كانت الرسالة تحتوي على رابط
    urls = re.findall(r'(https?://\S+)', event.message.message)
    
    if event.message.message == '/start':
        await event.respond(f'مرحبًا عزيزي {men} \n أرسل لي رابط الفيديو وسأقوم بتحميله لك')
    elif urls:
        # تحقق من الاشتراك في القنوات المطلوبة
        if not await check_subscription(user_id):
            await event.respond('يجب عليك الاشتراك في القنوات التالية لاستخدام هذا البوت:\n' + '\n'.join(REQUIRED_CHANNELS))
            return
        
        url = urls[0]
        status_message = await event.respond('**جاري تحميل الفيديو...**')
        
        video_path = download_video(url)
        if video_path:
            await client.send_file(event.chat_id, video_path)
            os.remove(video_path)
            await event.respond(f'**تم تحميل الفيديو بنجاح✅**')
        else:
            await event.respond('**فشل في تحميل الفيديو❌**')
        
        await status_message.delete()
    elif event.message.message == '/stats' and event.sender_id == DEVELOPER_ID:
        stats = get_statistics()
        stats_message = await format_statistics(stats)
        await event.respond(stats_message)

# بدء العميل
client.start()
client.run_until_disconnected()
