import random
import telebot

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Ти Путин!')


messages_about_putin = ['Ти Путин!', 'Нет, ти Путин!', 'За такие слова можно по лицу получить!',
                        'Это ты поддерживаешь Путина!', 'У меня на стуле Немцов чай пил!',
                        'Ты поддерживаешь путина!', 'Поддерживаешь Путина именно ты!', 'Следи за языком!',
                        'Путин это ти!', 'НЕЕЕЕЕЕТ! ТИ ПУТИН!!!1!']

messages_not_about_putin = ['За такие слова можно по лицу получить!', 'Следи за языком!',
                            'Здесь должно быть зеркало на моем месте, чтобы вы узнали, что такое "мерзкий"!',
                            'Я бы на месте Явлинского от стыда удавился!', 'Я честный человек!',
                            'Я дико извиняюсь', 'Может, я еще и путин?', 'А знаешь, кто еще так говорил? ПУТИН!']


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if 'путин' in message.text.lower():
        bot.send_message(message.chat.id, random.choice(messages_about_putin))
    else:
        bot.send_message(message.chat.id, random.choice(messages_not_about_putin))


@bot.message_handler(content_types=['sticker'])
def sticker_answer(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBc4Vgyowsv-217eFtdYCCdz7p2udeqAACdwEAAp6c1AXSYeGRV6WhyB8E')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBc4tgyoxGqAABG_qt6xRtsO4jN-XjThEAAngBAAKenNQFdO4FpstPWzQfBA')
    bot.send_message(message.chat.id, 'ЭТО ТИ!')


voice_messages = ['По голосу слышу - ти Путин!', 'Дежавю. Будто снова смотрю конференцию Путина',
                  'Знакомый голос... Путин?', 'Ти Путин!']


@bot.message_handler(content_types=['voice', 'video_note'])
def voice_answer(message):
    bot.send_message(message.chat.id, random.choice(voice_messages))


bot.polling()
