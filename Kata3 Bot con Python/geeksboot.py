from telegram.ext import Updater,CommandHandler

def main():
    updater=Updater(token="1155082026:AAHBYlC2LFfNP7s_iLIMj6014Qnz-T3K76M", use_context=True)

    # Añadimos ub manejador para el boton start
    updater.dispatcher.add_handler(CommandHandler("start",start))

    #Añadir manejador para el comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite",repite))

    #Añadir manejador para el comando /sumar
    updater.dispatcher.add_handler(CommandHandler("sumar",sumar))

    # Empezamos a pedir notificaciones a Telegram
    updater.start_polling()

    #Capturamos  señales de paradas
    updater.idle()

def start(update,context):
    update.message.reply_text("Hola, soy un bot")

def repite(update,context):
    update.message.reply_text(update.message.text)

def sumar(update,context):
    suma=int(context.args[0])+int(context.args[1])
    update.message.reply_text("El resultado es : "+str(suma))

main()