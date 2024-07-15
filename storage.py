import json
from datetime import datetime, timedelta

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "users": [],
            "groups": [],
            "banned_users": [],
            "messages": [],
            "daily_activity": {},
        }

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_user(user_id, is_group=False):
    data = load_data()
    if is_group:
        if user_id not in data["groups"]:
            data["groups"].append(user_id)
    else:
        if user_id not in data["users"]:
            data["users"].append(user_id)
    save_data(data)

def add_banned_user(user_id):
    data = load_data()
    if user_id not in data["banned_users"]:
        data["banned_users"].append(user_id)
    save_data(data)

def add_message(user_id):
    data = load_data()
    today = datetime.now().date().isoformat()
    if today not in data["daily_activity"]:
        data["daily_activity"][today] = {"users": [], "messages": 0}
    
    if user_id not in data["daily_activity"][today]["users"]:
        data["daily_activity"][today]["users"].append(user_id)
    
    data["daily_activity"][today]["messages"] += 1
    save_data(data)

def get_statistics():
    data = load_data()
    total_users = len(data["users"])
    total_groups = len(data["groups"])
    total_banned_users = len(data["banned_users"])
    today = datetime.now().date().isoformat()
    yesterday = (datetime.now() - timedelta(1)).date().isoformat()
    
    today_stats = data["daily_activity"].get(today, {"users": [], "messages": 0})
    yesterday_stats = data["daily_activity"].get(yesterday, {"users": [], "messages": 0})
    
    total_today_users = len(today_stats["users"])
    total_yesterday_users = len(yesterday_stats["users"])
    total_today_messages = today_stats["messages"]
    total_yesterday_messages = yesterday_stats["messages"]
    
    recent_users = [user for day in data["daily_activity"].values() for user in day["users"]]
    
    stats_message = f"""
    مرحبًا بك في قسم الإحصائيات 📊
    
    • المستخدمون:
    - العدد الإجمالي للمستخدمين: {total_users}
    - عدد المستخدمين في الخاص: {total_users - total_groups}
    - عدد القنوات والمجموعات: {total_groups}
    - عدد المحظورين: {total_banned_users}
    
    • التفاعل:
    
    - اليوم ({today}):
    - المستخدمون: {total_today_users}
    - المجموعات: {total_today_messages}
    - المستخدمون المتفاعلين: {total_today_users}
    - الرسائل: {total_today_messages}
    
    - في الأمس ({yesterday}):
    - المستخدمون: {total_yesterday_users}
    - المجموعات: {total_yesterday_messages}
    - المستخدمون المتفاعلين: {total_yesterday_users}
    
    - عدد المستخدمين الجدد اليوم: {total_today_users}
    - عدد المستخدمين الجدد الأمس: {total_yesterday_users}
    - عدد المستخدمين الجدد هذا الشهر: {total_today_users}
    - عدد المستخدمين الجدد الشهر الماضي: {total_yesterday_users}
    
    - قائمة اخر الاعضاء الذين تفاعلو :
    """ + "\n".join([str(user) for user in recent_users[:5]])
    
    return stats_message
