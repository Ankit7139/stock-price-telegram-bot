import telebot
from yahoo_fin import stock_info


API_KEY = '1803900826:AAFVDWPE_Bt_Boz0zT7xxwsWK8IQRX84IAI'
bot = telebot.TeleBot(API_KEY)



@bot.message_handler(commands=['start'])
def founder(message):
  bot.send_message(message.chat.id, "Welcome\nJust Enter the ticker Symbol of stock you want to search \nUse .ns extension at end of the ticker for NSE stocks")


def greetmsg(message):
  message=message.text.split()
  if(message[0].lower()=="hi"):
    return True;
  else:
    return False;

@bot.message_handler(func=greetmsg)
def sayhi(message):
  bot.send_message(message.chat.id, "Hi there! You have to just type the ticker")


def getTicker(message):
  message=message.text.split()
  global name
  name=message[0]
  global price
  try:
    price=stock_info.get_live_price(message[0])
  except:
    def sayTrue(message):
      return True
    @bot.message_handler(func=sayTrue)
    def showerror(message):
      bot.send_message(message.chat.id,"Sorry! Can't Find that.")
    return False
  return True


@bot.message_handler(func=getTicker)
def showprice(message):
  bot.send_message(message.chat.id,"The Price of "+name.upper()+" is: "+str(price)[0:6])


bot.polling()