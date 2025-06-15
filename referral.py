from telegram import Update
from telegram.ext import ContextTypes
import sqlite3
from config import DB_NAME

async def referral_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    username = update.message.from_user.username or f"user{user_id}"
    referral_code = f"{username}_{user_id}"

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create referrals table
    c.execute('''CREATE TABLE IF NOT EXISTS referrals (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    code TEXT
                )''')

    c.execute("INSERT OR IGNORE INTO referrals (user_id, username, code) VALUES (?, ?, ?)",
              (user_id, username, referral_code))
    conn.commit()
    conn.close()

    await update.message.reply_text(
        f"👥 *Your Referral Code:*\n`{referral_code}`\n\n"
        "📢 Share this code with friends to earn rewards!",
        parse_mode="Markdown"
    )