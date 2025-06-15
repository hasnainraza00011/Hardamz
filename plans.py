from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def plans_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🗓️ Daily Plan – $1", callback_data="daily_plan")],
        [InlineKeyboardButton("📅 Weekly Plan – $2.5", callback_data="weekly_plan")],
        [InlineKeyboardButton("📆 Monthly Plan – $5", callback_data="monthly_plan")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📌 *Choose a Subscription Plan:*",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def plan_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    plan_info = {
        "daily_plan": "🗓️ *Daily Plan* – $1\n✅ Unlimited Voice Access for 24 Hours.",
        "weekly_plan": "📅 *Weekly Plan* – $2.5\n✅ Unlimited Voice Access for 7 Days.",
        "monthly_plan": "📆 *Monthly Plan* – $5\n✅ Unlimited Voice Access for 30 Days."
    }

    message = plan_info.get(query.data, "❌ Invalid Plan.")
    await query.edit_message_text(text=message, parse_mode="Markdown")