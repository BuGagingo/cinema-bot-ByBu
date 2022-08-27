import datetime
import time
from service.mainDataBase import init, execute_data, execute_in_db
from service.shcedule import sql_fetch
from aiogram import Bot, executor, Dispatcher
import schedule

bot = Bot(token='5701301489:AAF_o_kE7MJzNtnBYFi4P4wy2cXNGVp1w9E')  # getenv
dp = Dispatcher(bot)
day = datetime.date.today()

# async def on_shutdown(dp):
#     await bot.close()


async def on_startup(dp):
    await bot.send_message(chat_id=869578795, text=f"Бот с расписанием на {day}, Готов к работе")


def start():
    init()
    execute_data()
    execute_in_db()
    sql_fetch()
    print('Сообщения к отправке готовы')


if __name__ == '__main__':
    try:
        print("\033[2;35;40mBOT STARTED\033[0m \n")
        start()
        schedule.every().day.at("09:00").do(start)
        from tgbot.cinema_bot import dp, set_default_commands
        from aiogram import executor
        executor.start_polling(dp, on_startup=on_startup)

    except Exception as ex:
        print('Cinema bot: Service stopped')
        print(ex)

    while True:
        schedule.run_pending()
        time.sleep(600)
