from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Defina a função para o comando /start
def start(update, context):
    update.message.reply_text("Olá! Eu sou um bot do Telegram. Envie /groupid para ver o ID deste grupo.")

# Defina a função para o comando /groupid
def groupid(update, context):
    chat_id = update.message.chat_id
    update.message.reply_text(f"O ID deste grupo é: {chat_id}")

# Função para lidar com mensagens não reconhecidas
def unknown(update, context):
    update.message.reply_text("Desculpe, não entendi esse comando.")

def main():
    # Substitua "SEU_TOKEN" pelo token do seu bot
    updater = Updater(token="SEU_TOKEN_BOT", use_context=True)
    dispatcher = updater.dispatcher

    # Handlers para comandos e mensagens não reconhecidas
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("groupid", groupid))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Inicie o bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
