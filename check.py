from telethon import TelegramClient, errors

# قائمة القنوات المطلوبة
REQUIRED_CHANNELS = ['@voltbots', '@ctktc']

# دالة للتحقق من الاشتراك في القنوات المطلوبة
async def check_subscription(client: TelegramClient, user_id: int) -> bool:
    for channel in REQUIRED_CHANNELS:
        try:
            # نحاول الحصول على معلومات عن القناة
            entity = await client.get_entity(channel)
            # نحاول الحصول على المشاركين في القناة والتحقق من وجود المستخدم بينهم
            participants = await client.get_participants(entity)
            if not any(participant.id == user_id for participant in participants):
                return False
        except errors.rpcerrorlist.UserNotParticipantError:
            # المستخدم ليس مشارك في القناة
            return False
        except Exception as e:
            print(f"Error checking subscription for channel {channel}: {e}")
            return False
    return True
