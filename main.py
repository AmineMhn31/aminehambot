import subprocess
import os
import logging
import asyncio
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

# ========================CIPHER==========================================
async def cipher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Should make this a Database probably
    # with open('user_ids','a') as file:
    #     file.write(f"{update.effective_chat.first_name} : {update.effective_chat.id}\n")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🐹")

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "🔢Today's Cipher Code 18/08/2024📅:\n*T:  ➖*\n*E:  🔘*\n*L:  🔘➖🔘🔘*\n*E:  🔘*\n*G:  ➖➖🔘*\n*R:  🔘➖🔘* \n*A:  🔘➖*\n*M:  ➖➖*\n✅CLAIM 1000000💰\.",
        parse_mode='MARKDOWNV2')

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
        "THE COMMANDES ARE :\n*/start*\n*/news*\n*/cipher*\n*/bike*\n*/clone*\n*/cube*\n*/train*\n*/all*\nThese will generate 4 keys for their respective games\.",
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
    generated_keys = [f"`{key}`" for key in keys]
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
    generated_keys = [f"`{key}`" for key in keys]
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
    generated_keys = [f"`{key}`" for key in keys]
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
    generated_keys = [f"`{key}`" for key in keys]
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
        generated_keys = [f"`{key}`" for key in keys]
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

    news_handler = CommandHandler('news', news, block=False)
    application.add_handler(news_handler)
    
    cipher_handler = CommandHandler('cipher', cipher, block=False)
    application.add_handler(cipher_handler)

    bike_handler = CommandHandler('bike', bike, block=False)
    application.add_handler(bike_handler)

    clone_handler = CommandHandler('clone', clone, block=False)
    application.add_handler(clone_handler)

    cube_handler = CommandHandler('cube', cube, block=False)
    application.add_handler(cube_handler)

    train_handler = CommandHandler('train', train, block=False)
    application.add_handler(train_handler)

    all_handler = CommandHandler('all', all, block=False)
    application.add_handler(all_handler)

    application.run_polling()
