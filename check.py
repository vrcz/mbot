from telethon import TelegramClient

# قائمة القنوات المطلوبة
REQUIRED_CHANNELS = ['@voltbots', '@ctktc']

# دالة للتحقق من الاشتراك في القنوات المطلوبة
async def check_subscription(client: TelegramClient, user_id: int) -> bool:
    for channel in REQUIRED_CHANNELS:
        try:
            participant = await client.get_participant(channel, user_id)
            if not participant:
                return False
        except Exception as e:
            print(f"Error checking subscription for channel {channel}: {e}")
            return False
    return True
