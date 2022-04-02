import telebot
import config
import random
import time

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welkome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🧡 Мой репозиторий")
    item2 = types.KeyboardButton("😋 Контактные данные")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет, {0.first_name}! я VizitQA_Bot".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

possible_answers = ['Хмм... неожиданно', 'Надо бы подумать', 'Не знаю)', 'Сложно сказать', 'К такому меня не готовили',
                    'Хо-Хо', 'У вас вся спина белая', 'Не учите меня жить', 'Мрак.', 'Кр-р-расота', 'Хамите.',
                    'Жди ответа до лета', 'Уля', 'Ого', 'Жуть!', 'ну ващще']



#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🧡 Мой репозиторий':
            bot.send_message(message.chat.id, 'https://github.com/KirillSarafannikov-QA')
        elif message.text == "😋 Контактные данные":

            markup = types.InlineKeyboardMarkup(row_width=4)
            item1 = types.InlineKeyboardButton("Telegram", url='https://t.me/Kirill_Sarafannikov')
            item2 = types.InlineKeyboardButton("Email", callback_data='E')
            item3 = types.InlineKeyboardButton("📞", callback_data='telephone')
            item4 = types.InlineKeyboardButton("😸 Мой кот", callback_data='cat')

            markup.add(item1, item2, item3, item4)
            bot.send_photo(message.chat.id, 'https://avatars.githubusercontent.com/u/101517517?v=4')
            bot.send_message(message.chat.id, 'Контактные данные', reply_markup=markup)

        elif message.text == "расскажи стихотворение":
            bot.send_message(message.chat.id, 'я сочиняю это стихотворение\nперед открытым окном куря\nего еще нет '
                                              'но уже не верю ему\nи не верил ни дня \n\nкак и всей поэзии впрочем\n'
                                              'сотворенной угодно когда\nэто просто подборки дурацких строчек\nчеловеку'
                                              ' нужна еда\n\nчеловеку нужны калории\nчтоб ногами крутить колесо\nесли '
                                              'кто-то поэт то горе ему\nпоэт ничего не несет\n\nни социального смысла'
                                              ' ни груза\nразве что чушь и бред\nдля человека поэт обуза\nстыдись поэт'
                                              '\n\nчеловеку ни горячо ни холодно\nни от ямба ни от хорея\nчеловеку и '
                                              'горячо и холодно\nот батареи\n\nчеловек должен жить подобающе\nчтоб '
                                              'давала тепло батарея\nс рождения и до самого кладбища\nтрудясь себя '
                                              'не жалея\n\nи тогда исполняются с лихвой\nего потребности базовые\n'
                                              'пока каждый нелепый стих твой\nнаполняется глупыми фразами\n\nпафосом '
                                              'желчью и клеветой\nи беспочвенными словами\nне имеющими отношения к '
                                              'простой\nжизни реальной\n\nстыдись поэт ты пустое место\nпустые '
                                              'сентенции издающее\nпока человек труда повсеместно\nкаждый день '
                                              'вкалывает предыдущего пуще\n\nа ты стоишь у окна открытого\nсмотришь '
                                              'на серость неба летнего\nстыдись небо не для того человеку выдано\n'
                                              'чтобы глазеть на него\n\nнебо на то нам повешено партией\nчтоб потолок'
                                              ' осознать было проще\nесли не можешь ты осознать его\nто место тебе на'
                                              ' площади\n\nгде человек собирается вечером\nчтобы на казни смотреть'
                                              ' как ты таких\nстыдись поэт петля тебе обеспечена\nпетли прочнее '
                                              'стихов твоих\n\nя завершаю это стихотворение\nу старой кофейни на '
                                              'входе\nи в чем-то уже даже верю ему\nвроде\n\n© Святослав Свидригайлов')

        else:
            bot.send_message(message.chat.id, possible_answers[random.randint(0, len(possible_answers)-1)])

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'telephone':
                bot.send_message(call.message.chat.id, '+79613349666\n+79024667036')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="📞Звони")
            elif call.data == 'E':
                bot.send_message(call.message.chat.id, 'ViVo-42@yandex.ru')
            elif call.data == 'cat':
                bot.send_photo(call.message.chat.id, 'https://sun9-62.userapi.com/impg/NB2oVHyuabM8GnnC_ht6uDVfh0L4pu1M'
                                                     '_PlOpg/1n5aBqtNFkM.jpg?size=720x1280&quality=95&sign=ae176e892dfa'
                                                     '85d41cc7c4f3c0e8e830&type=album')
                time.sleep(1)
                bot.send_photo(call.message.chat.id, 'https://sun9-79.userapi.com/impg/961qO9Ez_mMOkwJL8HG98REHDDd94GqJ'
                                                     'hkWVzA/3JCgCcfLHHw.jpg?size=1280x720&quality=96&sign=821dcc8308da'
                                                     'c17348e7a394e2cce039&type=album')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="😼Зубкииии😼")

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)