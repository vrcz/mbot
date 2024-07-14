import sqlite3
from datetime import datetime

# إنشاء اتصال بقاعدة البيانات وإنشاء الجداول إذا لم تكن موجودة
def initialize_db():
    conn = sqlite3.connect('bot_stats.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        first_seen TIMESTAMP,
                        last_seen TIMESTAMP
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        chat_id INTEGER,
                        timestamp TIMESTAMP,
                        FOREIGN KEY(user_id) REFERENCES users(user_id)
                      )''')

    conn.commit()
    return conn, cursor

conn, cursor = initialize_db()

def add_user(user_id):
    now = datetime.now()
    cursor.execute('INSERT OR IGNORE INTO users (user_id, first_seen, last_seen) VALUES (?, ?, ?)', (user_id, now, now))
    cursor.execute('UPDATE users SET last_seen = ? WHERE user_id = ?', (now, user_id))
    conn.commit()

def add_message(user_id, chat_id):
    now = datetime.now()
    cursor.execute('INSERT INTO messages (user_id, chat_id, timestamp) VALUES (?, ?, ?)', (user_id, chat_id, now))
    conn.commit()

def get_statistics():
    stats = {}
    
    cursor.execute('SELECT COUNT(*) FROM users')
    stats['total_users'] = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM users WHERE last_seen >= date("now", "-1 day")')
    stats['today_active_users'] = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM messages WHERE timestamp >= date("now", "-1 day")')
    stats['today_messages'] = cursor.fetchone()[0]

    cursor.execute('SELECT user_id FROM messages WHERE timestamp >= date("now", "-1 day") GROUP BY user_id ORDER BY COUNT(*) DESC LIMIT 5')
    stats['recent_active_users'] = [row[0] for row in cursor.fetchall()]

    return stats
