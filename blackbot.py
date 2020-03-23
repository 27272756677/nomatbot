import telebot

# Сюда пишем токен созданный BotFather
token='ваш токен'
# Создаем экземпляр бота
bot = telebot.TeleBot(token)
# Получаем айди чата по его имени
GROUP_ID=bot.get_chat('@имячата').id
# Список матов которые нужно удалять
blacklist=['бля','хуй','пизд','пидар','сука','суки']

# Перехват чужих сообщений в чате
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # По очереди ищем маты из списка в сообщении
    for x in blacklist:
        if(x in message.text):
            # Если найдены маты удаляем сообщение с ними
            bot.delete_message(message.chat.id, message.message_id)
        else:
            pass
        
if __name__ == "__main__":
    bot.infinity_polling()
