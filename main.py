import telebot
bot = telebot.TeleBot('6534066741:AAGv_ZwiRKPfXD6oi3FFtXhX06bDPdDbyVI')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '👋 *Привет!* Это бот, который расскажет тебе о тайне Олега, который работает в Умскул.\n\n_Для продолжение введи команду /continue._', parse_mode='Markdown')

@bot.message_handler(commands=['continue'])
def mail(message):
    bot.send_message(message.chat.id, '💰 На самом деле Олег скамер. Во время вебинара он смог украсть у Артёма *$500*. Какой кошмар. Правда же?\n\n_Для продолжения введи команду /continue2._', parse_mode='Markdown')

@bot.message_handler(commands=['continue2'])
def mail(message):
    bot.send_message(message.chat.id, '🧑‍💻 Также, Олег является создателем Midjourney, но скрывает этого и устроился работать в Умскул.\n\n_Для продолжения введи команду /continue3._', parse_mode='Markdown')

@bot.message_handler(commands=['continue3'])
def main(message):
    bot.send_message(message.chat.id, '🤯 Кроме всего этого, Олег держит Артёма в заложниках! Полное видео без регистрации можно глянуть [тут](https://www.youtube.com/watch?v=dQw4w9WgXcQ).\n\n_P.S. Весь материал, который представлен в боте - шуточный (хотя кто знает). Не воспринимайте всерьёз. Огромное спасибо _*Олегу*_ и _*Артёму*_! Очень крутые ребята! Всё класс объяснили, просто бомба. Куратор, прости что там много букв ❤️._', parse_mode='Markdown')

bot.infinity_polling()
