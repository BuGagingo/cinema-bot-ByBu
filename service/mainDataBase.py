import time

from API.commandsAPI import get_sessions, get_one_movies
import sqlite3
from sqlite3 import Error
import logging
import json

db_name = "cinema.db"
INIT_FILE = "service/init.sql"


def init():
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.executescript(open(INIT_FILE).read())
        conn.commit()
        print("Cinema bot: SqlLite started")
    except Error as ex:
        logging.error(ex)
    finally:
        if conn:
            conn.close()


def execute_data():
    print("Выгружаем данные с cmd.kz/api/v2")
    city_id = [2, 3]
    for city in city_id:
        try:
            sessions = get_sessions(city_id=str(city)).json()
            data = []
            for session in sessions:
                # print(session)
                data.append({
                    "id_session": session["id"],
                    "date_session": session["date"],
                    "city_id": city,
                    "url_session": session["web_url"],
                    "name_hall": session["hall"]["name"],
                    "id_movie": session["movie"]["id"],
                    "name_movie": session["movie"]["name"],
                    "url_poster_movie": session["movie"]["poster_url"],
                    "duration_movie": session["movie"]["duration"],
                    "status_session": "В процессе 🔄",
                    "deleted": False
                })
            with open(f"request_{str(city)}.json", "w", encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False)
        except Exception as ex:
            print(ex, "\nОшибка подключения")


def execute_in_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    city_id = ["2", "3"]
    for city in city_id:
        with open(f"request_{city}.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            for session in data:
                x = session.values()
                x = tuple(x)
                # print(x)
                cursor.executemany("INSERT INTO sessions VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (x,))
                conn.commit()
    print("Данные успешно загружены в Базу Данных")


# def polling():
# init()
# execute_data()
# execute_in_db()
