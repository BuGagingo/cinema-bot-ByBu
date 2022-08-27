import sqlite3

DB_NAME = 'cinema.db'
con = sqlite3.connect(DB_NAME)
schedule_day = {2: [], 3: []}
poster_url = {2: [], 3: []}
city_id = [2, 3]


def sql_fetch():
    cursorObj = con.cursor()
    # cursorObj.execute(f"SELECT * FROM sessions WHERE session_date Like'2022-08-17%'")
    for x in city_id:
        cursorObj.execute(f"SELECT * FROM sessions WHERE city_id Like'{str(x)}'")
        res = cursorObj.fetchall()
        count_schedule = len(res)
        if x == 2:
            print("Число сеансов в Алматы: ", str(count_schedule))
        else:
            print("Число сеансов в Шымкенте: ", str(count_schedule))
        # print(res)
        for row in res:
            hour = int(row[1][11:13])
            minute = int(row[1][14:16])
            if minute < 15:
                minute = minute + 60 - 15
                if hour == 0:
                    hour = 23
                else:
                    hour -= 1
            else:
                minute -= 15
            new_time = (str(hour) + ":" + str(minute))
            schedule_day[x].append(new_time)
            poster_url[x].append(row[7])
    # print(schedule_day, poster_url)
    print("Расписание на сегодня составлено")
    return schedule_day

# sql_fetch()
# print(poster_url)
