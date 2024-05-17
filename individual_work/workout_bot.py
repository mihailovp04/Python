import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

bot = telebot.TeleBot("7193440663:AAFv-WtYe9g42YWqTZ13yLFDUERTNQTkAHQ")

workouts = {
    'Понедельник': [
        'Отжимания: 3 подхода по 20 раз', 
        'Жим лежа: от минимального к максимальному весу',
        'Жим гантелей на наклонной скамье: 4 подхода по 12 раз', 
        'Разведение гантелей лежа: 4 подхода по 12 раз'
    ],
    'Вторник': [
        'Приседания: 3 подхода по 40', 
        'Выпады: 4 подхода по 20 раз', 
        'Жим ногами: 4 подхода по 15 раз', 
        'Сгибание ног в тренажере: 4 подхода по 12 раз'
    ],
    'Среда': [
        'Подтягивания: 3 подхода по 10 раз', 
        'Тяга верхнего блока: 4 подхода по 12 раз', 
        'Тяга в наклоне: 4 подхода по 12 раз', 
        'Становая тяга: 3 подхода по 10 раз'
    ],
    'Четверг': [
        'Жим гантелей сидя: 4 подхода по 12 раз', 
        'Разведение гантелей в стороны: 4 подхода по 15 раз', 
        'Передний подъем гантелей: 5 подходов по 10 раз'
    ],
    'Пятница': [
        'Сгибание рук со штангой: 4 подхода по 12 раз', 
        'Сгибание рук с гантелями: 4 подхода по 12 раз', 
        'Сгибание рук на скамье Скотта: 4 подхода по 12 раз', 
        'Концентрированное сгибание рук: 4 подхода по 15 раз'
    ],
    'Суббота': [
        'Отжимания на брусьях: 3 подхода по 20 раз', 
        'Жим на трицепс: 4 подхода по 12 раз', 
        'Французский жим: 3 подхода по 10 раз', 
        'Разгибание рук с гантелью за головой: 4 подхода по 12 раз'
    ],
    'Воскресенье': ['Сегодня вы можете спокойно отдыхать, до завтра!']
}

motivational_quotes = [
    "Запомни: всего одна ошибка - и ты ошибся. Д.Стэтхэм",
    "Делай как надо. Как не надо, не делай. Д.Стэтхэм",
    "Ваше тело может почти всё, важно только ваше желание.",
    "Только вы можете изменить свою жизнь, никто не сделает это за вас.",
    "Сильные люди создаются в трудные времена.",
    "Три слова - это два слова! Д.Стэтхэм"
]

workout_artists = [
    "AC/DC",
    "Eminem",
    "Metallica",
    "Kanye West",
    "Linkin Park",
    "Rammstein",
    "Imagine Dragons",
    "The Weeknd",
    "Skrillex",
    "Miyagi & Эндшпиль",
    "David Guetta"
]

def generate_markup():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(*(InlineKeyboardButton(day, callback_data=day) for day in workouts.keys()))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = (
        "Привет! Я ваш личный тренер-бот. Выберите день недели, чтобы получить тренировку:\n\n"
        "Вот несколько команд, которые могут вам помочь:\n"
        "/start - начать заново\n"
        "/help - получить помощь\n"
        "/quote - получить мотивационную цитату\n"
        "/music - получить список исполнителей для тренировки\n"
    )
    bot.send_message(message.chat.id, welcome_message, reply_markup=generate_markup())

@bot.message_handler(commands=['help'])
def send_help(message):
    help_message = (
        "Я помогу вам оставаться в форме! Вы можете использовать следующие команды:\n\n"
        "/start - начать заново\n"
        "/quote - получить мотивационную цитату\n"
        "/music - получить список исполнителей для тренировки\n"
        "Выберите день недели, чтобы получить программу тренировки."
    )
    bot.send_message(message.chat.id, help_message)

@bot.message_handler(commands=['quote'])
def send_quote(message):
    bot.send_message(message.chat.id, random.choice(motivational_quotes))

@bot.message_handler(commands=['music'])
def send_music(message):
    music_message = "Вот несколько исполнителей, которых можно слушать во время тренировки:\n" + '\n'.join(workout_artists)
    bot.send_message(message.chat.id, music_message)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    workout = workouts.get(call.data, ['Отдых или легкая кардио нагрузка'])
    response = f"Тренировка на {call.data}:\n" + '\n'.join(workout)
    bot.send_message(call.message.chat.id, response)

@bot.message_handler(func=lambda message: True)
def handle_unknown_command(message):
    unknown_command_message = (
        "Извините, я не знаю такой команды.\n\n"
        "Вот несколько команд, которые могут вам помочь:\n"
        "/start - начать заново\n"
        "/help - получить помощь\n"
        "/quote - получить мотивационную цитату\n"
        "/music - получить список исполнителей для тренировки\n"
        "Выберите день недели, чтобы получить программу тренировки."
    )
    bot.send_message(message.chat.id, unknown_command_message)

if __name__ == '__main__':
    bot.polling(none_stop=True)
