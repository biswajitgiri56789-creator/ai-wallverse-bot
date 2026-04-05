import requests
import random
import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

prompts = [
    "beautiful nature landscape 4k wallpaper ultra hd",
    "anime aesthetic wallpaper 4k ultra hd",
    "amoled dark minimal wallpaper black background 4k",
    "hindu god krishna shiva ganesha wallpaper 4k hd divine",
    "futuristic neon wallpaper 4k ultra hd trending"
]

async def start(update, context):
    await update.message.reply_text("Send me any wallpaper idea 🖼️")

async def generate(update, context):
    prompt = update.message.text
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    await update.message.reply_photo(photo=url)

async def auto_post(context):
    prompt = random.choice(prompts)
    url = f"https://image.pollinations.ai/prompt/{prompt}"

    caption = "✨ 4K AI Wallpaper\n📱 Download & Set Now 🔥"
    
    await context.bot.send_photo(chat_id=CHANNEL_ID, photo=url, caption=caption)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate))

app.job_queue.run_repeating(auto_post, interval=18000, first=10)

app.run_polling()
