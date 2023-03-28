import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Define a function to start the bot
def start(update, context):
    # Ask the user to enter an integer
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter an integer:")
    # Set the state to 'waiting_for_integer'
    context.user_data['state'] = 'waiting_for_integer'

# Define a function to handle user input
def handle_input(update, context):
    # Get the user input and store it in a variable 's'
    s = update.message.text
    # Convert 's' to an integer and store it in the user data
    context.user_data['s'] = int(s)
    # Check if s >= 1
    if s >= '1':
        # Ask 'question 1' with 2 possible answers 'yes' and 'no' shown as clickable buttons
        keyboard = [[InlineKeyboardButton("Yes", callback_data='q1_yes'),
                     InlineKeyboardButton("No", callback_data='q1_no')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Question 1: Do you want to add 50 to the variable?", reply_markup=reply_markup)
        # Set the state to 'waiting_for_q1_answer'
        context.user_data['state'] = 'waiting_for_q1_answer'
    else:
        # Ask 'question 2' with 2 possible answers 'yes' and 'no' shown as clickable buttons
        keyboard = [[InlineKeyboardButton("Yes", callback_data='q2_yes'),
                     InlineKeyboardButton("No", callback_data='q2_no')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Question 2: Do you want to add 20 to the variable?", reply_markup=reply_markup)
        # Set the state to 'waiting_for_q2_answer'
        context.user_data['state'] = 'waiting_for_q2_answer'

# Define a function to handle button clicks
def handle_button_click(update, context):
    query = update.callback_query
    # Get the value of the clicked button and store it in a variable 'answer'
    answer = query.data
    # Check the current state and update the user data accordingly
    if context.user_data['state'] == 'waiting_for_q1_answer':
        if answer == 'q1_yes':
            context.user_data['e'] = 50
        else:
            context.user_data['e'] = 0# Register the handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(handle_button_click))
dispatcher.add_handler(MessageHandler(Filters.text, handle_input))

# Start the bot
updater.start_polling()
updater.idle()

    elif context.user_data['state'] == 'waiting_for_q2_answer':
        if answer == 'q2_yes':
            context.user_data['e'] = 20
        else:
            context.user_data['e'] = 0
    # Check the value of 'e' and show the appropriate message
    if context.user_data['e'] == 0:
        context.bot.send_message(chat_id=query.message.chat_id, text="text1")
    elif context.user_data['e'] == 20:
        context.bot.send_message(chat_id=query.message.chat_id, text="text2")
    else:
        context.bot.send_message(chat_id=query.message.chat_id, text="text3")

# Create an Updater object and set up the handlers
updater = Updater(token='5486890272:AAEPDRADV5rVOLk7vRvRouXIi7Hkcc5V8RE', use_context=True)
dispatcher = updater

# Register the handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(handle_button_click))
dispatcher.add_handler(MessageHandler(Filters.text, handle_input))

# Start the bot
updater.start_polling()
updater.idle()