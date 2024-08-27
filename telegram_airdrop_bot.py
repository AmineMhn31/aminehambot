import os
import logging
import asyncio
import sys
import httpx
import random
import time
import uuid
import datetime
import stay_alive
from loguru import logger
import cryptocompare
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.background import BackgroundScheduler

# Token setup
TOKEN = "7474041486:AAFLRJZacez8OyYCn5bxta_itkiHiTZ07MU"  # Replace with your bot token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.CRITICAL)

# ====================== Daily Airdrop Function ==========================
async def daily_airdrop(context: ContextTypes.DEFAULT_TYPE):
    currencies = ["BTC", "ETH", "USDT", "BNB", "ADA", "XRP"]  # Add more currencies as needed
    message = "📊 **Cryptocurrency Update: Highs and Lows** 📊\n\n"

    try:
        for currency in currencies:
            history = cryptocompare.get_historical_price_day(currency, currency='USD', limit=1)
            if history:
                high_price = history[0]['high']
                low_price = history[0]['low']
                message += f"**{currency}**:\nHigh: ${high_price:.2f}\nLow: ${low_price:.2f}\n\n"

        await context.bot.send_message(chat_id='AMINEHAMBOT', text=message, parse_mode='MarkdownV2')

    except Exception as e:
        logging.error(f"Error in daily airdrop: {e}")

# ====================== /airdrop Command Handler ========================
async def airdrop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await daily_airdrop(context)  # Reuse the daily airdrop function for manual command
    await update.message.reply_text("Airdrop sent!")

# ====================== Main Function ===================================
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    # Scheduler for the airdrop every 5 minutes
    scheduler = BackgroundScheduler(timezone="UTC")
    scheduler.add_job(daily_airdrop, trigger='interval', minutes=5, args=[application.bot])
    scheduler.start()

    # Add command handlers (including the new /airdrop command)
    application.add_handler(CommandHandler("airdrop", airdrop_command))

    logging.info("Bot is starting...")
    application.run_polling()

