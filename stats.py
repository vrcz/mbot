from datetime import datetime, timedelta

# هذا هو معرف المطور
DEVELOPER_ID = 1373914665

async def format_statistics(stats):
    today = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    stats_message = f"""
مرحبًا بك في قسم الإحصائيات 📊

• المستخدمون:

- العدد الإجمالي للمستخدمين: {stats['total_users']}
- عدد المستخدمين المتفاعلين اليوم: {stats['today_active_users']}

• التفاعل:

- اليوم ({today}):

- المستخدمون المتفاعلين: {stats['today_active_users']}
- الرسائل: {stats['today_messages']}

- قائمة اخر الاعضاء الذين تفاعلو :
1. {stats['recent_active_users'][0] if len(stats['recent_active_users']) > 0 else 'N/A'}
2. {stats['recent_active_users'][1] if len(stats['recent_active_users']) > 1 else 'N/A'}
3. {stats['recent_active_users'][2] if len(stats['recent_active_users']) > 2 else 'N/A'}
4. {stats['recent_active_users'][3] if len(stats['recent_active_users']) > 3 else 'N/A'}
5. {stats['recent_active_users'][4] if len(stats['recent_active_users']) > 4 else 'N/A'}
    """
    return stats_message datetime

# هذا هو معرف المطور
DEVELOPER_ID = 1373914665

async def get_statistics(client):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    # هنا يجب عليك تنفيذ المنطق لجمع الإحصائيات المطلوبة
    # سأستخدم قيم افتراضية هنا كمثال

    stats = {
        'total_users': 100,
        'private_users': 70,
        'channels_and_groups': 30,
        'banned_users': 5,
        'today': today,
        'today_active_users': 10,
        'today_messages': 50,
        'yesterday': yesterday,
        'yesterday_active_users': 8,
        'new_users_today': 5,
        'new_users_yesterday': 3,
        'new_users_this_month': 50,
        'new_users_last_month': 40,
        'recent_active_users': [12345678, 23456789, 34567890, 45678901, 56789012]
    }

    return stats

async def format_statistics(stats):
    stats_message = f"""
مرحبًا بك في قسم الإحصائيات 📊

• المستخدمون:

- العدد الإجمالي للمستخدمين: {stats['total_users']}
- عدد المستخدمين في الخاص: {stats['private_users']}
- عدد القنوات والمجموعات: {stats['channels_and_groups']}
- عدد المحظورين: {stats['banned_users']}

• التفاعل:

- اليوم ({stats['today']}):

- المستخدمون المتفاعلين: {stats['today_active_users']}
- الرسائل: {stats['today_messages']}

- في الأمس ({stats['yesterday']}):

- المستخدمون المتفاعلين: {stats['yesterday_active_users']}

- عدد المستخدمين الجدد اليوم: {stats['new_users_today']}
- عدد المستخدمين الجدد الأمس: {stats['new_users_yesterday']}
- عدد المستخدمين الجدد هذا الشهر: {stats['new_users_this_month']}
- عدد المستخدمين الجدد الشهر الماضي: {stats['new_users_last_month']}

- قائمة اخر الاعضاء الذين تفاعلو :
1. {stats['recent_active_users'][0]}
2. {stats['recent_active_users'][1]}
3. {stats['recent_active_users'][2]}
4. {stats['recent_active_users'][3]}
5. {stats['recent_active_users'][4]}
    """
    return stats_message
