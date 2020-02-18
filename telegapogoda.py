import telebot
import pyowm 

owm = pyowm.OWM('affe09dd9ba0dc635779ed17bdf11f38', language = "ru")
bot = telebot.TeleBot("1089654967:AAGuzKfKrH1SEEstj3uIPbBMLOf3CYV38Io")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас в районе " + str(temp) + "\n\n"
	if temp < -5:
		answer += "Сейчас очень холодно, одевайся как танк!"
	elif (temp < 10)&(temp > 0):
		answer += "Сейчас холодно, оденься потеплее. "
	elif (temp < -5)&(temp > -1):
		answer += "Сейчас холодно, но не так холодно как при меньше нуля, но я не знаю как это у тебя там работает. "
	elif temp < 20:
		answer += "Специальное веселое значение"
	else:
		answer += "Температура норм, одевай платье. "

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop= True )