from telegram import Update, BotCommand
from telegram.ext import CommandHandler, CallbackContext
from telegram.error import BadRequest

# Initialize a global variable to track update mode
update_mode = False

def update_on(update: Update, context: CallbackContext) -> None:
    global update_mode
    update_mode = True
    update.message.reply_text("🔧 Bot is now under maintenance. All commands are disabled.")
    
    # Set all commands to empty or disable
    try:
        context.bot.set_my_commands([])
    except BadRequest as e:
        update.message.reply_text(f"Error: {e.message}")

def update_off(update: Update, context: CallbackContext) -> None:
    global update_mode
    update_mode = False
    update.message.reply_text("✅ Bot is now active. All commands are enabled.")
    
    # Set all commands back
    try:
        commands = [
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Get help"),
            BotCommand("airdrop", "Claim an airdrop"),
            # Add more commands here
        ]
        context.bot.set_my_commands(commands)
    except BadRequest as e:
        update.message.reply_text(f"Error: {e.message}")

def is_update_mode() -> bool:
    return update_mode

def add_update_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("updateON", update_on))
    dispatcher.add_handler(CommandHandler("updateOFF", update_off))
