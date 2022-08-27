import datetime
import sqlite3

DB_NAME = 'cinema.db'
con = sqlite3.connect(DB_NAME)
day = datetime.date.today()


def change_status(city_id):
    cursorObj = con.cursor()
    cursorObj.execute(f"DELETE FROM sessions WHERE city_id = {str(city_id)}")
    con.commit()
    cursorObj.close()


# print(check_status())

def message_tg():
    text = {2: [], 3: []}
    city_id = ["2", "3"]
    cursorObj = con.cursor()
    for city in city_id:
        cursorObj.execute(f"SELECT * FROM sessions WHERE city_id = '{city}'")
        res = cursorObj.fetchall()
        for row in res:
            text[int(city)].append(
                f'<b>Ссылка:</b> <a href=\'{row[3]}\'>ОТКРЫТЬ СЕАНС</a>\n<b>Фильм:</b> {row[6]}\n<b>Зал:</b> {row[4]}\n<b'
                f'>Время:</b> {row[1][11:16]}\n<b>Статус:</b> В Процессе 🔄')
    return text
