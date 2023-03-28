import telegram
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# Define the start function
def start(update, context):
    update.message.reply_text("Please enter an integer")
    s = int(update.message.text)
    return "integer"

# Define the integer handler function
def handle_integer(update, context):
    try:
        if s >= 1:
            return "q1"
        else:
            return "q2"
    except ValueError:
        update.message.reply_text("Invalid input. Please enter an integer.")
        return "integer"

# Define the first question handler function
def handle_q1(update, context):
    user_input = update.message.text.lower()
    if user_input == "yes":
        e = 50
        return "handle_text"
    elif user_input == "no":
        e = 0
        return "handle_text"
    else:
        update.message.reply_text("Invalid input. Please enter 'yes' or 'no'.")
        return "q1"

# Define the second question handler function
def handle_q2(update, context):
    user_input = update.message.text.lower()
    if user_input == "yes":
        e = 20
        return "handle_text"
    elif user_input == "no":
        e = 0
        return "handle_text"
    else:
        update.message.reply_text("Invalid input. Please enter 'yes' or 'no'.")
        return "q2"

# Define the text handler function
def handle_text(update, context):
    if e == 50:
        update.message.reply_text("text1")
    elif e == 20:
        update.message.reply_text("text2")
    else:
        update.message.reply_text("text3")

    return ConversationHandler.END

# Define the cancel function
def cancel(update, context):
    update.message.reply_text('Cancelled')

    return ConversationHandler.END

# Define the conversation handler
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        "integer": [MessageHandler(Filters.text & ~Filters.command, handle_integer)],
        "q1": [MessageHandler(Filters.regex('^(yes|no)$') & ~Filters.command, handle_q1)],
        "q2": [MessageHandler(Filters.regex('^(yes|no)$') & ~Filters.command, handle_q2)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

def main():
    TOKEN = "5486890272:AAEPDRADV5rVOLk7vRvRouXIi7Hkcc5V8RE"
    PORT = int(os.environ.get("PORT", 8443))
    APP_NAME = "cyprus-tax-bot"

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    conv_handler = MessageHandler(Filters.text & ~Filters.command, handle_integer)
    dp.add_handler(conv_handler)

    dp.add_handler(MessageHandler(Filters.regex("(?i)yes|no"), handle_q1))
    dp.add_handler(MessageHandler(Filters.regex("(?i)yes|no"), handle_q2))

    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://cyprus-tax-bot.herokuapp.com/5486890272:AAEPDRADV5rVOLk7vRvRouXIi7Hkcc5V8RE"
    )

    updater.idle()

if __name__ == '__main__':
    main()
