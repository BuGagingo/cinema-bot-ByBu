import asyncio
from service.admins_channels import admin, channel
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile, Message, CallbackQuery, InputMedia, \
    message, BotCommand
from service.executeDataBase import message_tg, change_status
from service.shcedule import poster_url, schedule_day, city_id, sql_fetch
import datetime

from start import start

bot = Bot(token='')  # getenv
dp = Dispatcher(bot)
count = 0
day = datetime.date.today()

async def set_default_commands():
    return await bot.set_my_commands(commands=[
        BotCommand('start', 'Запустить бота'),
        BotCommand('update_data', 'Обновить расписание на день')
    ])


@dp.callback_query_handler(text="yes_ok")
async def status_update(query: CallbackQuery):
    InlineKeyboardMarkup().clean()
    caption = query.message['caption']
    caption_entities = query.message['caption_entities']
    caption = caption[0:-12] + "Состоится ✅"
    await query.message.edit_caption(caption=caption, caption_entities=caption_entities)


@dp.callback_query_handler(text="no_ok")
async def status_update(query: CallbackQuery):
    # print(query)
    InlineKeyboardMarkup().clean()
    caption = query.message['caption']
    caption_entities = query.message['caption_entities']
    caption = caption[0:-12] + "Не состоится ❌"
    await query.message.edit_caption(caption=caption, caption_entities=caption_entities)


@dp.callback_query_handler(text="cancel")
async def status_update(query: CallbackQuery):
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Состоится ", callback_data="yes"),
        InlineKeyboardButton(text="Не состоится", callback_data="no")
    )
    caption = query.message['caption']
    caption_entities = query.message['caption_entities']
    await query.message.edit_caption(caption=caption, caption_entities=caption_entities, reply_markup=reply_markup)


@dp.callback_query_handler(text="yes")
async def status_update(query: CallbackQuery):
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Подтвердить ", callback_data="yes_ok"),
        InlineKeyboardButton(text="Отмена", callback_data="cancel")
    )
    caption = query.message['caption']
    caption_entities = query.message['caption_entities']
    await query.message.edit_caption(caption=caption, caption_entities=caption_entities, reply_markup=reply_markup)


@dp.callback_query_handler(text="no")
async def status_update(query: CallbackQuery):
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Подтвердить ", callback_data="no_ok"),
        InlineKeyboardButton(text="Отмена", callback_data="cancel")
    )
    caption = query.message['caption']
    caption_entities = query.message['caption_entities']
    await query.message.edit_caption(caption=caption, caption_entities=caption_entities, reply_markup=reply_markup)


@dp.message_handler(commands=['start'])
async def sendMessage(message: Message, count=count):
    if str(message.chat.id) in admin():
        for admin_id in admin():
            await bot.send_message(int(admin_id), text=f"Бот с расписанием на {day}, Запущен")
        while True:
            if datetime.datetime.now().time() > datetime.datetime.strptime(schedule_day[2][count], '%H:%M').time():
                reply_markup = InlineKeyboardMarkup().add(
                    InlineKeyboardButton(text="Состоится ", callback_data="yes"),
                    InlineKeyboardButton(text="Не состоится", callback_data="no")
                )
                if poster_url[2][count] is None:
                    poster_url[2][count] = "https://upload.wikimedia.org/wikipedia/ru/thumb/a/ac/No_image_available.svg/1200px-No_image_available.svg.png"
                await bot.send_photo(
                    chat_id=channel()[0],
                    photo=poster_url[2][count],
                    reply_markup=reply_markup,
                    caption=message_tg()[2][count],
                    parse_mode="HTML",
                )
                # change_status()
                count += 1
            await asyncio.sleep(15)


# @dp.message_handler(commands=['start_shimkent'])
# async def sendMessage(message: Message, count=count):
#     print("Бот работает")
#     if message.chat.id in admins_id:
#         await bot.send_message(message.chat.id, text="Бот запущен")
#         while True:
#             if datetime.datetime.now().time() > datetime.datetime.strptime(schedule_day[3][count], '%H:%M').time():
#                 reply_markup = InlineKeyboardMarkup().add(
#                     InlineKeyboardButton(text="Состоится ", callback_data="yes"),
#                     InlineKeyboardButton(text="Не состоится", callback_data="no")
#                 )
#                 if poster_url[3][count] is None:
#                     poster_url[3][count] = "https://upload.wikimedia.org/wikipedia/ru/thumb/a/ac/No_image_available.svg/1200px-No_image_available.svg.png"
#                 await bot.send_photo(
#                     chat_id=964922954,
#                     photo=poster_url[3][count],
#                     reply_markup=reply_markup,
#                     caption=message_tg()[3][count],
#                     parse_mode="HTML",
#                 )
#                 # change_status()
#                 count += 1
#             await asyncio.sleep(15)

# @dp.message_handler(commands=['change_status'])
# async def change_status():
#     await


@dp.message_handler(commands=['update_data'])
async def update_data(message: Message):
    if message.chat.id in admins_id:
        await bot.send_message(chat_id=message.chat.id, text="Данные перезаписаны запустите бота /start")
        await start()


# @dp.callback_query_handler(text="yes")
# async def status_update(query: CallbackQuery, count=count):
#     InlineKeyboardMarkup().clean()
#     await query.message.edit_caption(caption=message_tg(status="Состоится ✅")[count], parse_mode="HTML")
#
#
# @dp.callback_query_handler(text="no")
# async def status_update(query: CallbackQuery):
#     InlineKeyboardMarkup().clean()
#     await query.message.edit_caption(caption=message_tg(status="Не состоится ❌")[count], parse_mode="HTML")


# if __name__ == '__main__':
#     executor.start_polling(dp)
