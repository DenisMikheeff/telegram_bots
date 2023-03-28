from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text("Please enter an integer:")
    return "integer"

def handle_integer(update, context):
    try:
        s = int(update.message.text)
        if s >= 1:
            update.message.reply_text("Question 1: Yes or No?")
            return "q1"
        else:
            update.message.reply_text("Question 2: Yes or No?")
            return "q2"
    except ValueError:
        update.message.reply_text("Invalid input. Please enter an integer.")
        return "integer"

def handle_q1(update, context):
    answer = update.message.text.lower()
    if answer == "yes":
        context.user_data["q1"] = True
        context.user_data["q2"] = False
        context.user_data["e"] = 50
        update.message.reply_text("Answer saved. Thank you.")
    elif answer == "no":
        context.user_data["q1"] = False
        context.user_data["q2"] = True
        context.user_data["e"] = 20
        update.message.reply_text("Answer saved. Thank you.")
    else:
        update.message.reply_text("Invalid answer. Please enter 'Yes' or 'No'.")

def handle_q2(update, context):
    answer = update.message.text.lower()
    if answer == "yes":
        context.user_data["q1"] = False
        context.user_data["q2"] = True
        context.user_data["e"] = 20
        update.message.reply_text("Answer saved. Thank you.")
    elif answer == "no":
        context.user_data["q1"] = False
        context.user_data["q2"] = False
        context.user_data["e"] = 0
        update.message.reply_text("Answer saved. Thank you.")
    else:
        update.message.reply_text("Invalid answer. Please enter 'Yes' or 'No'.")

    if context.user_data["e"] == 0:
        update.message.reply_text("text1")
    elif context.user_data["e"] == 20:
        update.message.reply_text("text2")
    else:
        update.message.reply_text("text3")

def main():
    updater = Updater("YOUR_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    conv_handler = MessageHandler(Filters.text & ~Filters.command, handle_integer)
    dp.add_handler(conv_handler)

    dp.add_handler(MessageHandler(Filters.regex("(?i)yes|no"), handle_q1))
    dp.add_handler(MessageHandler(Filters.regex("(?i)yes|no"), handle_q2))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()