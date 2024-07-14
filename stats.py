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
    return stats_message
