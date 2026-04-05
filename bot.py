import requests
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "@yourchannelusername"

prompts = [
    "beautiful nature landscape 4k wallpaper ultra hd",
    "anime aesthetic wallpaper 4k ultra hd",
    "amoled dark minimal wallpaper black background 4k",
    "hindu god krishna shiva ganesha wallpaper 4k hd divine",
    "futuristic neon wallpaper 4k ultra hd trending"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me any wallpaper idea 🖼️")

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    await update.message.reply_photo(photo=url, caption=f"✨ {prompt}")

async def auto_post(context: ContextTypes.DEFAULT_TYPE):
    prompt = random.choice(prompts)
    url = f"https://image.pollinations.ai/prompt/{prompt}"

    caption = "✨ 4K AI Wallpaper\n📱 Download & Set Now 🔥\n\n#wallpaper #4k #ai #amoled #anime #nature #god"
    
    await context.bot.send_photo(chat_id=CHANNEL_ID, photo=url, caption=caption)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate))

# Auto পোস্ট scheduler (every 5 hours approx)
app.job_queue.run_repeating(auto_post, interval=18000, first=10)

app.run_polling()