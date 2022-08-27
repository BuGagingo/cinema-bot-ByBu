import sqlite3
from sqlite3 import Error

db_name = "cinema.db"


def admin():
    with open("admin.txt", "r") as file:
        admins_id = file.readline().split()
        return admins_id


def channel():
    with open("channels.txt", "r") as file:
        channels = file.readline().split()
        return channels
