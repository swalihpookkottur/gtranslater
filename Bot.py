from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('1861685728:AAE7BMdyBxTQl12Eqx6oAktQNZ7lDo1eyAk',use_context = True )

def start(updater,context):
 updater.message.reply_text('Hey, Iam Malayalam Translater... By @Swalihpookkottur Just send me A Word or A sentence.... I Will translate it to malayalam......   Powered by @diseno_Editzz')
def echo(updater,context):
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='ml') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
