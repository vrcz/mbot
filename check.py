from telethon import TelegramClient, errors

# قائمة القنوات المطلوبة
REQUIRED_CHANNELS = ['@voltbots', '@ctktc']

# دالة للتحقق من الاشتراك في القنوات المطلوبة
async def check_subscription(client: TelegramClient, user_id: int) -> bool:
    for channel in REQUIRED_CHANNELS:
        try:
            # نحاول الحصول على معلومات عن القناة
            entity = await client.get_entity(channel)
            # نحاول الحصول على مشارك في القناة
            participant = await client.get_participant(entity, user_id)
            if not participant:
                return False
        except errors.rpcerrorlist.UserNotParticipantError:
            # المستخدم ليس مشارك في القناة
            return False
        except Exception as e:
            print(f"Error checking subscription for channel {channel}: {e}")
            return False
    return True
