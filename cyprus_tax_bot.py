import telegram
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

def start(update, context):
    update.message.reply_text("Please enter an integer:")
    return "integer"

def handle_integer(update, context):
    try:
        s = int(update.message.text)
        if s >= 1:
            context.user_data["q1"] = True
            return "q1"
        else:
            context.user_data["q2"] = True
            return "q2"
    except ValueError:
        update.message.reply_text("Invalid input. Please enter an integer.")
        return "integer"

def handle_q1(update, context):
    answer = update.message.text.lower()
    if answer == "yes":
        context.user_data["e"] = 50
        update.message.reply_text("Answer saved. Thank you.")
        return ConversationHandler.END
    elif answer == "no":
        context.user_data["e"] = 0
        update.message.reply_text("Answer saved. Thank you.")
        return ConversationHandler.END
    else:
        update.message.reply_text("Invalid answer. Please enter 'Yes' or 'No'.")
        return "q1"

def handle_q2(update, context):
    answer = update.message.text.lower()
    if answer == "yes":
        context.user_data["e"] = 20
        update.message.reply_text("Answer saved. Thank you.")
        return ConversationHandler.END
    elif answer == "no":
        context.user_data["e"] = 0
        update.message.reply_text("Answer saved. Thank you.")
        return ConversationHandler.END
    else:
        update.message.reply_text("Invalid answer. Please enter 'Yes' or 'No'.")
        return "q2"

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        "integer": [MessageHandler(Filters.text & ~Filters.command, handle_integer)],
        "q1": [MessageHandler(Filters.text & ~Filters.command, handle_q1)],
        "q2": [MessageHandler(Filters.text & ~Filters.command, handle_q2)]
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