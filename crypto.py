import subprocess
import os
import logging
import asyncio
import httpx
import re
import cryptocompare
from PIL import Image
from io import BytesIO
from binance.client import Client
from bs4 import BeautifulSoup
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update, InputFile
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import requests
from stay_alive import keep_alive
# Paste Token Here if you don't wanna put it in an env. variable for some reason
TOKEN_INSECURE = "7474041486:AAFLRJZacez8OyYCn5bxta_itkiHiTZ07MU"

if os.name == 'posix':
    TOKEN = subprocess.run(["printenv", "HAMSTER_BOT_TOKEN"],
                           text=True,
                           capture_output=True).stdout.strip()
elif os.name == 'nt':
    TOKEN = subprocess.run(["echo", "%HAMSTER_BOT_TOKEN%"],
                           text=True,
                           capture_output=True,
                           shell=True).stdout.strip()
    TOKEN = "" if TOKEN == "%HAMSTER_BOT_TOKEN%" else TOKEN

AUTHORIZED_USERS = []
EXCLUSIVE = False

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.CRITICAL)


#=====================Markets===================================

async def markets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Example API call to CoinGecko for market data
        response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': 'false'
        })

        data = response.json()

        # Create the message with formatted market overview
        message = "📊 *Markets Overview*\n\n"
        message += "💹 *Trading Data*\n"
        for coin in data[:3]:  # Fetch the first 3 coins for trading data
            name = coin['name'].replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
            symbol = coin['symbol'].upper().replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
            price = f"{coin['current_price']:.2f}".replace(".", r"\.")
            percentage_change = f"{coin['price_change_percentage_24h']:.2f}".replace(".", r"\.").replace("-", r"\-")
            message += f"🔹 {name} \({symbol}\): ${price} \({percentage_change}%\)\n"
        
        message += "\n🔥 *Hot Coins*\n"
        for coin in data[3:6]:  # Next 3 coins for hot coins section
            name = coin['name'].replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
            symbol = coin['symbol'].upper().replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
            price = f"{coin['current_price']:.2f}".replace(".", r"\.")
            percentage_change = f"{coin['price_change_percentage_24h']:.2f}".replace(".", r"\.").replace("-", r"\-")
            message += f"🔸 {name} \({symbol}\): ${price} \({percentage_change}%\)\n"

        message += "\n🆕 *New Listing*\n"
        for coin in data[6:9]:  # Next 3 coins for new listings section
            name = coin['name'].replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
            symbol = coin['symbol'].upper().replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
            price = f"{coin['current_price']:.2f}".replace(".", r"\.")
            percentage_change = f"{coin['price_change_percentage_24h']:.2f}".replace(".", r"\.").replace("-", r"\-")
            message += f"🆕 {name} \({symbol}\): ${price} \({percentage_change}%\)\n"

        message += "\n📈 *Top Gainer Coin*\n"
        # Sort to find the top gainer
        top_gainer = max(data, key=lambda x: x['price_change_percentage_24h'])
        name = top_gainer['name'].replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
        symbol = top_gainer['symbol'].upper().replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
        price = f"{top_gainer['current_price']:.2f}".replace(".", r"\.")
        percentage_change = f"{top_gainer['price_change_percentage_24h']:.2f}".replace(".", r"\.").replace("-", r"\-")
        message += f"🏅 {name} \({symbol}\): ${price} \({percentage_change}%\)\n"

        message += "\n📉 *Top Volume Coin*\n"
        # Sort to find the highest volume coin
        top_volume = max(data, key=lambda x: x['total_volume'])
        name = top_volume['name'].replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
        symbol = top_volume['symbol'].upper().replace("(", r"\(").replace(")", r"\)").replace("-", r"\-")
        price = f"{top_volume['current_price']:.2f}".replace(".", r"\.")
        percentage_change = f"{top_volume['price_change_percentage_24h']:.2f}".replace(".", r"\.").replace("-", r"\-")
        message += f"🏆 {name} \({symbol}\): ${price} \({percentage_change}%\)\n"

        await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='MarkdownV2')

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"❌ An error occurred: {e}")

        
#=====================square===================================

async def square(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Define the list of currencies you want to compare
        currencies = ['BTC', 'ETH', 'USDT', 'SOL', 'USDC', 'TON', 'TRX', 'DOGE', 'BNB', 'XRP']  # Add or modify as needed
        currency_prices = []

        # Fetch square prices for each currency
        for currency in currencies:
            price_data = cryptocompare.get_price(currency, currency='USD')
            if price_data and 'USD' in price_data[currency]:
                current_price = price_data[currency]['USD']
                squared_price = current_price ** 2  # Calculate square of the price
                currency_prices.append((currency, squared_price))

        # Sort currencies by squared price in descending order
        sorted_currencies = sorted(currency_prices, key=lambda x: x[1], reverse=True)

        # Select the top 8 currencies
        top_currencies = sorted_currencies[:10]

        # Create the message with emojis
        message = "📈 *Top 10 Currencies by Squared Price:*\n 🚀"
        for currency, squared_price in top_currencies:
            message += f"💰 {currency}: {squared_price:.2f} USD²\n"

        # Escape special characters for MarkdownV2
        message = message.replace(".", "\\.").replace("-", "\\-").replace("(", "\\(").replace(")", "\\)")

        await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='MARKDOWNV2')

    except Exception as e:
        # Escape special characters in the error message as well
        error_message = f"❌ An error occurred: {e}"
        error_message = error_message.replace(".", "\\.").replace("-", "\\-").replace("(", "\\(").replace(")", "\\)")

        await context.bot.send_message(chat_id=update.effective_chat.id, text=error_message, parse_mode='MARKDOWNV2')

#=====================rate_currency===================================
async def rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Usage: /rate <currency>\nExample: /rate USDT")
        return

    try:
        currency = context.args[0].upper()

        # Fetch the current price of the currency in USD
        price_data = cryptocompare.get_price(currency, currency='USD')

        if price_data and 'USD' in price_data[currency]:
            current_price = price_data[currency]['USD']

            # Define your threshold for what you consider 'high' or 'low'
            high_threshold = 1.02  # Example threshold for high rate
            low_threshold = 0.98   # Example threshold for low rate

            # Compare current price with the thresholds
            if current_price > high_threshold:
                message = f"{currency} is currently HIGH at ${current_price} USD."
            elif current_price < low_threshold:
                message = f"{currency} is currently LOW at ${current_price} USD."
            else:
                message = f"{currency} is currently NORMAL at ${current_price} USD."

            await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Could not retrieve the price for {currency}.")

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"An error occurred: {e}")

#=====================convert_currency===================================
async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Usage: /convert <amount> <from_currency>/<to_currency>\nExample: /convert 100 USDT/BTC")
        return

    try:
        # Extract amount and currencies from user input
        amount = float(context.args[0])
        from_currency, to_currency = context.args[1].upper().split('/')

        # Fetch the conversion rate
        conversion_rate = cryptocompare.get_price(from_currency, currency=to_currency)

        if conversion_rate and to_currency in conversion_rate[from_currency]:
            converted_amount = amount * conversion_rate[from_currency][to_currency]
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"{amount} {from_currency} is approximately {converted_amount:.8f} {to_currency}."
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Could not retrieve conversion rate for {from_currency} to {to_currency}."
            )

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"An error occurred: {e}")



    # ==================================command================================

async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Should make this a Database probably
    # with open('user_ids','a') as file:
    #     file.write(f"{update.effective_chat.first_name} : {update.effective_chat.id}\n")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "THE COMMANDES ARE :\n*/crypto*\n*/markets*\n*/square*\n*/convert*\n*/rate*\n",
        parse_mode='MARKDOWNV2')


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN or TOKEN_INSECURE).build()
    server.logger.info("Server is running. Awaiting users...")

    
    crypto_handler = CommandHandler('crypto', crypto, block=False)
    application.add_handler(crypto_handler)

    markets_handler = CommandHandler('markets', markets, block=False)
    application.add_handler(markets_handler)
    
    square_handler = CommandHandler('square', square, block=False)
    application.add_handler(square_handler)
    
    convert_handler = CommandHandler('convert', convert, block=False)
    application.add_handler(convert_handler)

    rate_handler = CommandHandler('rate', rate, block=False)
    application.add_handler(rate_handler)
    


    application.run_polling()
