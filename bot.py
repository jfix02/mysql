from concurrent.futures import process


import telebot
import mysql.connector

#Imports all 

bot = telebot.TeleBot("5525873985:AAGcvcmMYqXH3i-8cZYSeqzAGsv_xJSEVLI")

#token

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
      database='base'
)
 #connect mysql



cursor = db.cursor()





user_data = {}


class User:
    def __init__(self,first_name):
        self.first_name =first_name
        self.last_name= '' 
    
#class 

@bot.message_handler(commands=['start','help'])

def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Send name") 
    bot.register_next_step_handler(msg, process_firstname_step)

#send message

def process_firstname_step(message):

    try:
        user_id = message.from_user.id
        user_data[user_id]=User(message.text)

        

        msg = bot.send_message(message.chat.id, "Send Your Surname")

        bot.register_next_step_handler(msg, process_lastname_step) 
        
    except Exception as e:

        bot.reply_to(message,"eror")
        



# send who your name










def process_lastname_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.last_name = message.text

        sq1 = "INSERT INTO user (first_name, last_name,user_id)\
                                 VALUES (%s, %s,%s)"
        val = (user.first_name,user.last_name,user_id)
        cursor.execute(sq1,val)
        db.commit()
        
        bot.send_message(message.chat.id, "You have successfully registered")
    except Exception as e:
        bot.reply_to(message, 'you are already registered')

#function regist




# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)





