import os
from telethon import TelegramClient, events
import yt_dlp
import re
import asyncio

from config import API_ID, API_HASH, BOT_TOKEN

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

# حدث لمعالجة الأوامر
@client.on(events.NewMessage)
async def handler(event):
    id = event.sender_id
    men = f"[{event.sender.first_name}](tg://user?id={id})"
    # تحقق مما إذا كانت الرسالة تحتوي على رابط
    urls = re.findall(r'(https?://\S+)', event.message.message)
    
    if event.message.message == '/start':
        await event.respond(f'مرحبًا عزيزي {men} \n أرسل لي رابط الفيديو وسأقوم بتحميله لك')
    elif urls:
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

# بدء العميل
client.start()
client.run_until_disconnected()
