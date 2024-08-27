import subprocess
import os
import logging
import asyncio
import httpx
import cryptocompare
from PIL import Image
from io import BytesIO
from telegram import Update, InputFile
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import server
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
# ========================COMBO==========================================
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = BytesIO(response.content)
        return image_data

async def combo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://raw.githubusercontent.com/AmineMhn31/aminehambot/main/combodzhamster.png")
        return

    url = context.args[0]
    try:
        image_data = await fetch_image(url)
        img = Image.open(image_data)
        img_format = img.format  # Get the image format to retain the original extension

        with BytesIO() as output:
            img.save(output, format=img_format)
            output.seek(0)
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=InputFile(output, filename=f"image.{img_format.lower()}"))

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Here is the image you requested.")

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Failed to retrieve image: {e}")

# ========================Mini Game==========================================
async def fetch_image(url: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = BytesIO(response.content)
        return image_data

async def minigame(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://raw.githubusercontent.com/AmineMhn31/aminehambot/main/minigame.png")
        return

    url = context.args[0]
    try:
        image_data = await fetch_image(url)
        img = Image.open(image_data)
        img_format = img.format  # Get the image format to retain the original extension

        with BytesIO() as output:
            img.save(output, format=img_format)
            output.seek(0)
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=InputFile(output, filename=f"image.{img_format.lower()}"))

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Here is the image you requested.")

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Failed to retrieve image: {e}")

# ========================CIPHER==========================================
async def cipher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "🔢Today's Cipher Code \(DUROV\) 26/08/2024📅:\n\*D:  ➖🔘🔘\*\n\*U:  🔘🔘➖\*\n\*R:  🔘➖🔘\*\n\*O:  ➖➖➖\*\n\*V:  🔘🔘🔘➖\*\n✅CLAIM 1000000💰\.",
        parse_mode='MARKDOWNV2'
    )


    # ==================================================================

# ========================NEWS==========================================
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Should make this a Database probably
    # with open('user_ids','a') as file:
    #     file.write(f"{update.effective_chat.first_name} : {update.effective_chat.id}\n")

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
🐹 السادة الرؤساء التنفيذيون،

🔑 قبل بضعة أسابيع، أطلقنا قسم Playground، وهو نموذج أولي لنظام Hamster الترفيهي المستقبلي\. تم دمج العديد من الألعاب مؤخرًا مع Hamster Kombat من خلال آلية المفاتيح\.

🎁 نريد توضيح أن المفاتيح ستؤثر على حجم الإنزال الجوي ولكنها ليست مطلوبة للمشاركة\. لمنع الاحتيال، لا يمكننا الكشف عن مزيد من التفاصيل الآن، لكننا نراقب عن كثب خدمات توليد المفاتيح ونسجل جميع القطع الأثرية التي تم الحصول عليها بشكل غير نزيه\. سيتم أخذ هذا في الاعتبار للإسقاطات الجوية القادمة\!

⚙️ يمكنك معرفة المزيد حول كيفية عمل Playground، وما الغرض منه وقليلًا عن الخطط المستقبلية\.
""",
        parse_mode='MARKDOWNV2'
    )

    # ==================================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Should make this a Database probably
    # with open('user_ids','a') as file:
    #     file.write(f"{update.effective_chat.first_name} : {update.effective_chat.id}\n")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "THE COMMANDES ARE :\n*/start*\n*/square*\n*/convert*\n*/rate*\n*/news*\n*/cipher*\n*/combo*\n*/minigame*\n*/bike*\n*/clone*\n*/cube*\n*/train*\n*/merge*\n*/twerk*\n*/poly*\n*/mow*\n*/mud*\n*/all*\nThese will generate 4 keys for their respective games\.",
        parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "You can also set how many keys are generated\. For example, */cube 8* will generate *EIGHT* keys for the cube game\.",
        parse_mode='MARKDOWNV2')
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=" ⚠️REMARK⚠️ : 🔰 BOT 100% SAFE ✅",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="🇩🇿 🇩🇿 POWERED BY 🇩🇿 🇩🇿",
                                   parse_mode='MARKDOWNV2')


async def bike(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳\.\.\.",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.",
        parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=1, no_of_keys=no_of_keys)
    generated_keys = [f"{key}" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")


async def clone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳\.\.\.",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.",
        parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=2, no_of_keys=no_of_keys)
    generated_keys = [f"{key}" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")


async def cube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳\.\.\.",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.",
        parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=3, no_of_keys=no_of_keys)
    generated_keys = [f"{key}" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")


async def train(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳\.\.\.",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.",
        parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=4, no_of_keys=no_of_keys)
    generated_keys = [f"{key}" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")

async def mergeaway(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳\.\.\.",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.",
        parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=5, no_of_keys=no_of_keys)
    generated_keys = [f"{key}" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")

async def twerkrace(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳\.\.\.",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.",
        parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=6, no_of_keys=no_of_keys)
    generated_keys = [f"{key}" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")

async def polysphere(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳\.\.\.",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.",
        parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=7, no_of_keys=no_of_keys)
    generated_keys = [f"{key}" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")
    
async def mowandtrim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳\.\.\.",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.",
        parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=8, no_of_keys=no_of_keys)
    generated_keys = [f"{key}" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")

async def mudracing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"⌛️Generating⏳\.\.\.",
                                   parse_mode='MARKDOWNV2')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"⏱️🙆‍♂ This will only take a moment 🙆‍♂⏱️\.\.\.",
        parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    keys = await server.run(chosen_game=9, no_of_keys=no_of_keys)
    generated_keys = [f"{key}" for key in keys]
    formatted_keys = '\n'.join(generated_keys)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{formatted_keys}",
                                   parse_mode='MARKDOWNV2')
    server.logger.info("Message sent to the client.")


async def all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if EXCLUSIVE and not update.effective_chat.id in AUTHORIZED_USERS:
        return

    server.logger.info(f"Generating for client: {update.effective_chat.id}")
    server.logger.info(f"Generating keys for All Games.")

    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Currently generating for all games\.\.\.",
        parse_mode='MARKDOWNV2')
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Come Back in about 5\-10 minutes\.",
                                   parse_mode='MARKDOWNV2')

    no_of_keys = int(context.args[0]) if context.args else 4
    server.logger.info(
        f"Number of keys set to {no_of_keys}. Context args was {'not empty' if context.args else 'empty'}"
    )

    # This currently overloads the server with login requests
    # tasks = [bike(update, context), clone(update, context), cube(update, context), train(update, context)]
    # await asyncio.gather(*tasks)

    for i in range(4):
        keys = await server.run(chosen_game=i + 1, no_of_keys=no_of_keys)
        generated_keys = [f"{key}" for key in keys]
        formatted_keys = '\n'.join(generated_keys)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"{formatted_keys}",
                                       parse_mode='MARKDOWNV2')
        server.logger.info("Message sent to the client.")


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN or TOKEN_INSECURE).build()
    server.logger.info("Server is running. Awaiting users...")

    
    start_handler = CommandHandler('start', start, block=False)
    application.add_handler(start_handler)

    square_handler = CommandHandler('square', square, block=False)
    application.add_handler(square_handler)
    
    convert_handler = CommandHandler('convert', convert, block=False)
    application.add_handler(convert_handler)

    rate_handler = CommandHandler('rate', rate, block=False)
    application.add_handler(rate_handler)
    
    news_handler = CommandHandler('news', news, block=False)
    application.add_handler(news_handler)

    combo_handler = CommandHandler('combo', combo, block=False)
    application.add_handler(combo_handler)
    
    cipher_handler = CommandHandler('cipher', cipher, block=False)
    application.add_handler(cipher_handler)
    
    minigame_handler = CommandHandler('minigame', minigame, block=False)
    application.add_handler(minigame_handler)

    bike_handler = CommandHandler('bike', bike, block=False)
    application.add_handler(bike_handler)

    clone_handler = CommandHandler('clone', clone, block=False)
    application.add_handler(clone_handler)

    cube_handler = CommandHandler('cube', cube, block=False)
    application.add_handler(cube_handler)

    train_handler = CommandHandler('train', train, block=False)
    application.add_handler(train_handler)

    mergeaway_handler = CommandHandler('merge', mergeaway, block=False)
    application.add_handler(mergeaway_handler)

    twerkrace_handler = CommandHandler('twerk', twerkrace, block=False)
    application.add_handler(twerkrace_handler)
    
    polysphere_handler = CommandHandler('poly', polysphere, block=False)
    application.add_handler(polysphere_handler)
      
    mowandtrim_handler = CommandHandler('mow', mowandtrim, block=False)
    application.add_handler(mowandtrim_handler)
    
    mudracing_handler = CommandHandler('mud', mudracing, block=False)
    application.add_handler(mudracing_handler)
    
    all_handler = CommandHandler('all', all, block=False)
    application.add_handler(all_handler)

    application.run_polling()
