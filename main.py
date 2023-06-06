import gc

import telebot
import gspread
from telebot import types, callback_data

"""маркетплэйс => утконос -  промежуточный результат"""

token = '5606338688:AAE4OFukJr5-2jJTIggzpGmYLTa_2ZEfGUE'
gc = gspread.service_account(filename='/home/unotuno/python/pet_projects/bot_markt_sale/markt-937992-2e27e8e4ce2d.json')
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1FhYGE5IODqbtXSfQGBs0BGUaUJYAWBGAC2SRWqYzf6M/edit#gid=0')

def start_bot(token):
    bot = telebot.TeleBot(token)

    def searchi(call):
        s = sht2.sheet1.findall(callback_data)
        bot.send_message(chat_id=call.message.chat.id, text='Чтобы воспользоваться акцией необходимо: перейти'
                                                            ' по ссылке или скопировать промокод и ввести его'
                                                            ' на сайте или приложении магазина')
        for i in s:
            k = sht2.sheet1.row_values(i.row)
            bot.send_message(chat_id=call.message.chat.id,
                             text=f'{k}')

    @bot.message_handler(commands=['start'])
    def main_menu(message):
        """inline main keybord for bot"""
        level_1 = types.InlineKeyboardMarkup(row_width=1)
        market = types.InlineKeyboardButton(text='Маркетплэйс', callback_data='marketplace')
        bank = types.InlineKeyboardButton(text='Бонусы от банков', callback_data='bank')
        invest = types.InlineKeyboardButton(text='Инвестиции', callback_data='invest')
        goods = types.InlineKeyboardButton(text='Доставка/продукты', callback_data='goods')
        pharmacy = types.InlineKeyboardButton(text='Аптеки/здоровье', callback_data='pharmacy')
        cafe = types.InlineKeyboardButton(text='Кафе/рестораны', callback_data='cafe')
        flowers = types.InlineKeyboardButton(text='Цветы', callback_data='flowers')
        online_service = types.InlineKeyboardButton(text='Онлайн сервис/поддержка', callback_data='online_service')
        shoes = types.InlineKeyboardButton(text='Обувь', callback_data='shoes')
        parfume = types.InlineKeyboardButton(text='Косметика/парфюмерия', callback_data='parfume')
        taxi = types.InlineKeyboardButton(text='Такси/каршеринг', callback_data='taxi')
        insurance = types.InlineKeyboardButton(text='Страхование', callback_data='insurance')
        hotels = types.InlineKeyboardButton(text='Авиабилеты/гостиницы', callback_data='hotels')
        sheet = types.InlineKeyboardButton(text='Таблица со всеми Промокодами', callback_data='sheet', url='https://docs.google.com/'
                                                                                                                    'spreadsheets/d/1FhYGE5IOD'
                                                                                                                    'qbtXSfQGBs0BGUaUJYAWBGAC2SR'
                                                                                                                    'WqYzf6M/edit#gid=0')
        level_1.add(market, bank, invest, goods, pharmacy, cafe, flowers, online_service, shoes, parfume, taxi, insurance, hotels, sheet)
        bot.send_message(message.chat.id, 'Choose category for sale \u2B07', reply_markup=level_1)


    @bot.callback_query_handler(func=lambda call: True)



    def inline_callback(call):
        """  callback inline keybord for marketplace  """
        if call.data == 'marketplace':
            level_market = types.InlineKeyboardMarkup(row_width=1)
            yandex = types.InlineKeyboardButton(text='Яндекс Маркет', callback_data='yandex')
            sber = types.InlineKeyboardButton(text='Сбермегамеркет', callback_data='sber')
            mvideo = types.InlineKeyboardButton(text='МВидео', callback_data='mvideo')
            eldorado = types.InlineKeyboardButton(text='Эльдорадо', callback_data='eldorado')
            mts = types.InlineKeyboardButton(text='МТС', callback_data='mts')
            wildberries = types.InlineKeyboardButton(text='Wildberries', callback_data='Wildberries')
            utkonos = types.InlineKeyboardButton(text='Утконос', callback_data='utkonos')
            zoozavr = types.InlineKeyboardButton(text='Зоозавр ТГ', callback_data='zoozavr')
            four_paws = types.InlineKeyboardButton(text='Четыре лапы', callback_data='four_paws')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_market.add(yandex, sber, mvideo, eldorado, mts, wildberries, utkonos, zoozavr, four_paws, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id,  text = 'please choose next...', reply_markup=level_market)

        elif call.data == 'bank':
            level_bank = types.InlineKeyboardMarkup(row_width=1)
            alpha = types.InlineKeyboardButton(text='Альфа-Банк', callback_data='alpha')
            vtb = types.InlineKeyboardButton(text='ВТБ', callback_data='vtb')
            gazprombank = types.InlineKeyboardButton(text='Газпромбанк', callback_data='gazprombank')
            tinkoff_inst = types.InlineKeyboardButton(text='Tinkoff инст', callback_data='tinkoff_inst')
            tinkoff = types.InlineKeyboardButton(text='Tinkoff', callback_data='tinkoff')
            homecredit = types.InlineKeyboardButton(text='Home Credit', callback_data='homecredit')
            mtsbank = types.InlineKeyboardButton(text='МТС банк', callback_data='mtsbank')
            openbank = types.InlineKeyboardButton(text='Открытие банк', callback_data='openbank')
            renesansbank = types.InlineKeyboardButton(text='Ренессанс кредит', callback_data='renesansbank')
            rosbank = types.InlineKeyboardButton(text='Росбанк', callback_data='rosbank')
            tochkabank = types.InlineKeyboardButton(text='Точка банк', callback_data='tochkabank')
            ubrirbank = types.InlineKeyboardButton(text='УБРиР ТГ', callback_data='ubrirbank')
            uralbank = types.InlineKeyboardButton(text='Уралсиб', callback_data='uralbank')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_bank.add(alpha, vtb, gazprombank, tinkoff_inst, tinkoff, homecredit, mtsbank, openbank, renesansbank,
                           rosbank, tochkabank, ubrirbank, uralbank, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='please choose next...', reply_markup=level_bank)

        elif call.data == 'invest':
            level_invest = types.InlineKeyboardMarkup(row_width=1)
            tinkoff_invest = types.InlineKeyboardButton(text='Тинькофф Инвестиции', callback_data='tinkoff_invest')
            freedom_finance = types.InlineKeyboardButton(text='Freedom Finance', callback_data='freedom_finance')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_invest.add(tinkoff_invest, freedom_finance, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_invest)

        elif call.data == 'goods':
            level_goods = types.InlineKeyboardMarkup(row_width=1)
            azbuka_vkusa = types.InlineKeyboardButton(text='Азбука вкуса', callback_data='azbuka_vkusa')
            auchan = types.InlineKeyboardButton(text='Ашан', callback_data='auchan')
            vkusvil = types.InlineKeyboardButton(text='ВкусВилл', callback_data='vkusvil')
            vinlab = types.InlineKeyboardButton(text='Винлаб', callback_data='vinlab')
            globus = types.InlineKeyboardButton(text='Глобус', callback_data='globus')
            delivery = types.InlineKeyboardButton(text='Delivery Club', callback_data='delivery')
            delivery_restauraunt = types.InlineKeyboardButton(text='Delivery Club из ресторанов', callback_data='delivery_restauraunt')
            sbermarket = types.InlineKeyboardButton(text='Сбермаркет', callback_data='sbermarket')
            lenta = types.InlineKeyboardButton(text='Лента онлайн', callback_data='lenta')
            magnit = types.InlineKeyboardButton(text='Магнит', callback_data='magnit')
            metro = types.InlineKeyboardButton(text='Metro', callback_data='metro')
            omoloko = types.InlineKeyboardButton(text='ОмолокО (Чистая линия)', callback_data='omoloko')
            fiveshop = types.InlineKeyboardButton(text='Пятёрочка', callback_data='fiveshop')
            perekrestok = types.InlineKeyboardButton(text='Перекрёсток', callback_data='perekrestok')
            perekrestok_vprok = types.InlineKeyboardButton(text='Перекрёсток Впрок', callback_data='perekrestok_vprok')
            pokupkin = types.InlineKeyboardButton(text='Покупкин', callback_data='pokupkin')
            samokat = types.InlineKeyboardButton(text='Самокат', callback_data='samokat')
            yandex_lavka = types.InlineKeyboardButton(text='Яндекс Лавка', callback_data='yandex_lavka')
            yandex_eda = types.InlineKeyboardButton(text='Яндекс Еда', callback_data='yandex_eda')
            yandex_restauraunt = types.InlineKeyboardButton(text='Яндекс Еда рестораны', callback_data='yandex_restauraunt')
            zdorovaya_voda = types.InlineKeyboardButton(text='Здоровая вода', callback_data='zdorovaya_voda')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_goods.add(azbuka_vkusa, auchan, vkusvil, vinlab, globus, delivery, delivery_restauraunt, sbermarket, lenta,
                             magnit, metro, omoloko, fiveshop, perekrestok, perekrestok_vprok, pokupkin, samokat, yandex_lavka,
                            yandex_eda, yandex_restauraunt, zdorovaya_voda,   menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_goods)

        elif call.data == 'pharmacy':
            level_pharmacy = types.InlineKeyboardMarkup(row_width=1)
            apteka_ru = types.InlineKeyboardButton(text='Аптека.ру', callback_data='apteka_ru')
            apteka_sklad = types.InlineKeyboardButton(text='Аптека от склада', callback_data='apteka_sklad')
            uteka = types.InlineKeyboardButton(text='Ютека', callback_data='uteka')
            sber_health = types.InlineKeyboardButton(text='Сбер Здоровье', callback_data='sber_health')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_pharmacy.add(apteka_ru, apteka_sklad, uteka, sber_health, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_pharmacy)

        elif call.data == 'cafe':
            level_cafe = types.InlineKeyboardMarkup(row_width=1)
            burger_king = types.InlineKeyboardButton(text='Бургер Кинг', callback_data='burger_king')
            kfc = types.InlineKeyboardButton(text='KFC', callback_data='kfc')
            dominos_pizza = types.InlineKeyboardButton(text='Domino\'s pizza', callback_data='dominos_pizza')
            food_band = types.InlineKeyboardButton(text='FoodBand', callback_data='food_band')
            your_pizza = types.InlineKeyboardButton(text='TVOЯ пицца', callback_data='your_pizza')
            tanuki = types.InlineKeyboardButton(text='Тануки', callback_data='tanuki')
            akitoria = types.InlineKeyboardButton(text='Якитория', callback_data='akitoria')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_cafe.add(burger_king, kfc, dominos_pizza, food_band, your_pizza, tanuki, akitoria, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_cafe)

        elif call.data == 'flowers':
            level_flowers = types.InlineKeyboardMarkup(row_width=1)
            flor_2_you = types.InlineKeyboardButton(text='Flor2U', callback_data='flor_2_you')
            russian_flowers = types.InlineKeyboardButton(text='Русский букет', callback_data='russian_flowers')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_flowers.add(flor_2_you, russian_flowers, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_flowers)

        elif call.data == 'online_service':
            level_online_service = types.InlineKeyboardMarkup(row_width=1)
            vk_music = types.InlineKeyboardButton(text='Vk музыка', callback_data='vk_music')
            yandex_music = types.InlineKeyboardButton(text='Яндекс музыка', callback_data='yandex_music')
            pocket = types.InlineKeyboardButton(text='Пакет', callback_data='pocket')
            fire = types.InlineKeyboardButton(text='Огонь', callback_data='fire')
            okko = types.InlineKeyboardButton(text='Okko', callback_data='okko')
            kinopoisk = types.InlineKeyboardButton(text='Кинопоиск', callback_data='kinopoisk')
            start = types.InlineKeyboardButton(text='Start', callback_data='start')
            premier = types.InlineKeyboardButton(text='Premier', callback_data='premier')
            yandex_multi = types.InlineKeyboardButton(text='Яндекс плюс мульти', callback_data='yandex_multi')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_online_service.add(vk_music, yandex_music, pocket, fire, okko, kinopoisk, start, premier, yandex_multi, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_online_service)

        elif call.data == 'shoes':
            level_shoes = types.InlineKeyboardMarkup(row_width=1)
            kari = types.InlineKeyboardButton(text='Kari', callback_data='kari')
            zenden = types.InlineKeyboardButton(text='Zenden', callback_data='zenden')
            sportmaster = types.InlineKeyboardButton(text='Спортмастер', callback_data='sportmaster')
            terranova = types.InlineKeyboardButton(text='Terranova', callback_data='terranova')
            tamaris = types.InlineKeyboardButton(text='Tamaris', callback_data='tamaris')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_shoes.add(kari, zenden, sportmaster, terranova, tamaris, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_shoes)

        elif call.data == 'parfume':
            level_parfume = types.InlineKeyboardMarkup(row_width=1)
            letual = types.InlineKeyboardButton(text='Летуаль', callback_data='letual')
            green_apple = types.InlineKeyboardButton(text='Золотое Яблоко', callback_data='green_apple')
            magnit_cosmetic = types.InlineKeyboardButton(text='Магнит Косметик', callback_data='magnit_cosmetic')
            podruzhka = types.InlineKeyboardButton(text='Подружка', callback_data='podruzhka')
            samokat_beauty = types.InlineKeyboardButton(text='Самокат Бьюти', callback_data='samokat_beauty')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_parfume.add(letual, green_apple, magnit_cosmetic, podruzhka, samokat_beauty, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_parfume)

        elif call.data == 'taxi':
            level_taxi = types.InlineKeyboardMarkup(row_width=1)
            maksim = types.InlineKeyboardButton(text='Такси Максим', callback_data='maksim')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_taxi.add(maksim, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_taxi)

        elif call.data == 'insurance':
            level_insurance = types.InlineKeyboardMarkup(row_width=1)
            tinkoff_insurance_avto = types.InlineKeyboardButton(text='Тинькофф Страхование Авто', callback_data='tinkoff_insurance_avto')
            sber_insurance_avto = types.InlineKeyboardButton(text='Сбер Страхование Авто', callback_data='sber_insurance_avto')
            sber_insurance_home = types.InlineKeyboardButton(text='Сбер Страхование Жилье', callback_data='sber_insurance_home')
            sravni_ru = types.InlineKeyboardButton(text='Сравни.ру', callback_data='sravni_ru')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_insurance.add(tinkoff_insurance_avto, sber_insurance_avto, sber_insurance_home, sravni_ru, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_insurance)

        elif call.data == 'hotels':
            level_hotels = types.InlineKeyboardMarkup(row_width=1)
            tinkoff_travel = types.InlineKeyboardButton(text='Тинькофф Путешествия', callback_data='tinkoff_travel')
            travelata = types.InlineKeyboardButton(text='Travelata', callback_data='travelata')
            sutochno_ru = types.InlineKeyboardButton(text='Суточно.ру', callback_data='sutochno_ru')
            yandex_travel = types.InlineKeyboardButton(text='Яндекс путешествия', callback_data='yandex_travel')
            menu = types.InlineKeyboardButton(text='В меню', callback_data='back_menu')
            level_hotels.add(tinkoff_travel, travelata, sutochno_ru, yandex_travel, menu)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='please choose next...', reply_markup=level_hotels)

        elif call.data == 'back_menu':
            level_1 = types.InlineKeyboardMarkup(row_width=1)
            market = types.InlineKeyboardButton(text='Маркетплэйс', callback_data='marketplace')
            bank = types.InlineKeyboardButton(text='Бонусы от банков', callback_data='bank')
            invest = types.InlineKeyboardButton(text='Инвестиции', callback_data='invest')
            goods = types.InlineKeyboardButton(text='Доставка/продукты', callback_data='goods')
            pharmacy = types.InlineKeyboardButton(text='Аптеки/здоровье', callback_data='pharmacy')
            cafe = types.InlineKeyboardButton(text='Кафе/рестораны', callback_data='cafe')
            flowers = types.InlineKeyboardButton(text='Цветы', callback_data='flowers')
            online_service = types.InlineKeyboardButton(text='Онлайн сервис/поддержка', callback_data='online_service')
            shoes = types.InlineKeyboardButton(text='Обувь', callback_data='shoes')
            parfume = types.InlineKeyboardButton(text='Косметика/парфюмерия', callback_data='parfume')
            taxi = types.InlineKeyboardButton(text='Такси/каршеринг', callback_data='taxi')
            insurance = types.InlineKeyboardButton(text='Страхование', callback_data='insurance')
            hotels = types.InlineKeyboardButton(text='Авиабилеты/гостиницы', callback_data='hotels')
            sheet = types.InlineKeyboardButton(text='Таблица со всеми Промокодами', callback_data='sheet',
                                               url='https://docs.google.com/'
                                                   'spreadsheets/d/1FhYGE5IOD'
                                                   'qbtXSfQGBs0BGUaUJYAWBGAC2SR'
                                                   'WqYzf6M/edit#gid=0')
            level_1.add(market, bank, invest, goods, pharmacy, cafe, flowers, online_service, shoes, parfume, taxi,
                        insurance, hotels, sheet)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Choose category for sale \u2B07', reply_markup=level_1)

        elif call.data == 'utkonos':
            s = sht2.sheet1.findall('Утконос')
            bot.send_message(chat_id=call.message.chat.id, text='Чтобы воспользоваться акцией необходимо: перейти'
                                                                ' по ссылке или скопировать промокод и ввести его'
                                                                ' на сайте или приложении магазина')
            for i in s:

                k = sht2.sheet1.row_values(i.row)
                bot.send_message(chat_id=call.message.chat.id,
                                 text=f'{k}')
                print(type(k))
            level_1 = types.InlineKeyboardMarkup(row_width=1)
            market = types.InlineKeyboardButton(text='Маркетплэйс', callback_data='marketplace')
            level_1.add(market)
            bot.send_message(chat_id=call.message.chat.id,
                                  text='back to level 2', reply_markup=level_1)
    bot.polling(none_stop=True)



if __name__ == "__main__":
    start_bot(token)