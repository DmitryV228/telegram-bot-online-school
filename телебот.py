#Установите необходимые библиотеки для работы бота
#pip install pyTelegramBotAPI
#pip install schedule
#pip install threading

#Импорт необходимых библиотек
import telebot
import schedule
import threading
import time


api_token = '7476398776:AAEWPcL5etUnii7PBmyJdd8zkKudSW1NfBc'
tg_channel = '@vsymirka'
bot = telebot.TeleBot(api_token)

#Обозначение списка сообщений (уроков)
messages = [
    """Сегодня нас ждет увлекательное путешествие в мир Древнего Востока. Какие страны существовали? Как люди жили? Во что верили? Обо всем этом в видеуроке: 
https://rutube.ru/video/private/3c5e268db67ac5ed49687d6fd91390a7/?p=VEkPq-vaUtVV_2QCQ2b6Xw

p.s: кино на сегодня:
- Принц Египта 1998 г
- Цинь Шихуанди. Правитель вечной империи 2017
- сериал Махабхарата [боги и герои индусов] 2013-2014 гг.""",

    """Античность — база истории, культуры,  математики, физики, медицины и так далее, и так далее...
Вперед смотреть новый урок!
https://rutube.ru/video/private/c1741bbb6754b0fcb0078be8f51da863/?p=2f6kecTGLiOqRIXxHbC4lw

p.s: кино на сегодня:
- Астерикс и Обеликс: Миссия Клеопатра 2002 г.
- 300 спартанцев 2006 г. 
- сериал Рим 2005-2007 г.""",

    """Внимание! Племена германцев напали на Европу и образовывают свои государства! Время переселений!
Cегодня пройдем Средневековье, скорее открывай видеоурок
https://rutube.ru/video/private/d39acd761c11fd95f403cc26126aacf4/?p=FXOkXI3ZN6lIm0qOhWuIoQ

p.s. кино на сегодня:
-Жанна Д'Арк 1999 г.
- Царство Небесное 2005 г.
- Лекарь. Ученик Авиценны 2013 г.
- Монгол 2007 г.
- Проклятье золотого цветка 2006 г.""",

    """Если вы не купили индульгенцию у Папы Римского, то вы точно сгорите в аду! Бууууу! Реформация вступает в дело, давайте посмотрим, как она изменит мир!
https://rutube.ru/video/private/ba421d9bedabec57ed290e3c500ec75f/?p=EZycYxEwF7ARFIIKnlgyjg

p.s. кино на сегодня:
- Ещё одна из рода Болейн 2008 г.
- Две королевы 2018 г.
- сериал Белая Королева 2013 г. 
- Версаль 2018 г. """,

    """Просвещение. Просвещение. Просвещение! Даруем Просвещение!
Самое время узнать, что это такое на уроке по XVIII веку
https://rutube.ru/video/private/34b508eb34c79ce9ff752c2b5cabd601/?p=VzTeKs68m28PRTFJNsPsnw

ps. кино на сегодня:
- Жанна Дюбари 2023 г.
- Мария Терезия 2017 г. 
- Один король - одна Франция 2018 г.
- сериал Сыны Свободы 2015 г. """,

    """Неужели мы добрались до XIX века? Да здравмтвует Викторианская эпоха и искусство! 
https://rutube.ru/video/private/4be8b2cd303509868acf9aeb6ceaa75f/?p=jwviVUVH3REVjOBf6IZ1TQ

p.s. кино на сегодня:
- Людвиг Баварский 2012 г.
‐ Наполеон 2023 г. 
- сериал Виктория 2016 г.
- Последний самурай 2003 г. """,

    """20 век — время неспокойное, тяжелое... Столько событий объединяет жизни миллионов людей. Важно не забывать о них:

ps. кино на сегодня:
- На Западном фронте без перемен 2022 г. 
- Пианист 2002 г.
- Сопротивление банкира 2018 г. 
- Дюнкерк 2017 г.
- Мальчик в полосатой пижаме 2008 г. 
- Мемуары Гейши 2005 г  """,

    """Пора восстанавливать порядок. Это не просто: колонии отделяются, холодная война разрастается. Ниточками события преплетяются в современность: 
https://rutube.ru/video/private/f417dd4a80d8dc047e137cf76d8910a4/?p=Aw4eK-51mFrUL82cgtaHIA

p.s. кино на сегодня:
- Шпионский мост 2015 г.
- Ливан 2009 г.
- Линия фронта 2011 [события корейской войны] 
- Взвод 1986 г. [события Вьетнамской войны] """,

    """Устраивайтесь поудобнее, налейте себе чая или кофе : сегодня созерцаем искусство 
https://rutube.ru/video/private/ab78e0225e806151d6dff0fa9bca5153/?p=pARWjQcXPr2ubkIXrVtCHQ'

p.s. кино на сегодня: 
- Леонардо да Винчи. Неизведанные миры 2019 г. 
- Ренуар. Последняя любовь 2012 г.
- Мистер Тёрнер 2014 г.
-сериал Отчаянные романтики 2009г.
- Полночь в Париже 2011 г.
- Общество мёртвых поэтов 1989 г."""
]

#Список для записи активных пользователей
user_message_index = {}

#Проверка на наличие неотправленных сообщений из списка
def send_message():
    for chat_id, index in list(user_message_index.items()):
        if index < len(messages):
            bot.send_message(chat_id, messages[index])
            user_message_index[chat_id] += 1
        if user_message_index[chat_id] >= len(messages):
            bot.send_message(chat_id, "Все сообщения отправлены. Спасибо за внимание!")
            del user_message_index[chat_id]

#Необходимая логика для работы планировщика задач
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

#Отправка первого (базового) сообщения и получения chat_id пользователя
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    if chat_id not in user_message_index:
        user_message_index[chat_id] = 0
        bot.send_message(chat_id, text=f'''Historia est magistra vita — история это учительница жизни
         
Совсем скоро перед тобой откроются новые вершины истории. Мысли, чувства, идеи людей прошлого превращали обычный день в историческое событие!

Но сначала вопрос-ответ:

1.Как будет происходить обучение? 
—Каждый день в 10:00 в этом боте будет присылаться ссылка на видеоурок и файл pdf-презентации 

2. Будут ли домашки? 
— Нет! Но если сильно хочется, можно посмотреть исторический фильм/сериал по пройденному периоду. Список будет чуть позже 

3. Сохраняются ли записи уроков после окончания курса? 
– Да, причем навсегда 

4. Можно ли выучить всю всемирную историю за этот курс? 
— К сожалению, не получится. Ведь нужно запомнить столько дат, личностей и событий. Это не значит, что выучить всеобщую историю невозможно — периодически повторяй информацию, тогда она обязательно отложиться в голове! 

5. В этом году сдаю ЕГЭ. Как все выучить? 
— Периодически повторяй информацию. Например: пройди курс в августе-октябре, пересмотри уроки в январе, повтори важные события в марте и перед самим экзаменом. Тогда ты точно сможешь придумать аргумент на сравнение всеобщей и отечественной истории! 

Кстати, автор курса ведет  бесплатный телеграмм-канал по всеобщей истории, можешь тоже туда подписаться: {tg_channel}''')

    else:
        bot.send_message(chat_id, "Вы уже подписаны на рассылку сообщений.")


#Запуск планировщика задач
schedule.every().day.at("10:00").do(send_message)

#Вынесения планировщика в отдельный поток для корректного выполнения
threading.Thread(target=run_schedule).start()

#Запуск бота
bot.polling(none_stop=True)