import requests
import datetime

url = "https://cdm.kz/api/v2/"
day = datetime.date.today()

# # '''Select city'''
# def select_city():
#     Almaty = "2"
#     Shimkent = "3"

# '''List of films with nested sessions'''
def get_movies(city_id="2"):
    return requests.get(f'{str(url)}movies?city_id={str(city_id)}&date={day}')


# print(get_movies().text)


# '''List of sessions with nested films'''
def get_sessions(city_id):
    return requests.get(f'{str(url)}sessions?city_id={str(city_id)}&date={day}')


# print(get_sessions(2).json())

# Details the movie
def get_one_movies(movie_id):
    try:
        r = requests.get(f'{str(url)}movies/{str(movie_id)}')
    except Exception as ex:
        print(ex, "\n Movie not found")
        r = None
    return r

# # Получения списка залов с вложенными сеансами
# def get_holles(city_id):
#     if city_id is None:
#         city_id = '2'
#     return requests.get('https://cdm.kz/api/v2/halls?city_id=' + city_id)
#
#
# # Получения плана мест в зале
# def get_plan_holle(id):
#     if id is None:
#         return None
#     return requests.get('https://cdm.kz/api/v2/sessions/' + id)
#
#
# # Получения занятых мест в зале
# def get_plan_holle_status(id):
#     if id is None:
#         return None
#     return requests.get('https://cdm.kz/api/v2/sessions/' + id + '/status')
#
#
# # Получение списка премьер с вложенными сеансами
# def get_premieres(city_id):
#     if city_id is None:
#         city_id = '2'
#     return requests.get('https://cdm.kz/api/v2/premieres?city_id=' + city_id)
#
#
# # Детали премьеры
# def get_one_premiere(id, city_id):
#     if city_id and id is None:
#         return None
#     return requests.get('https://cdm.kz/api/v2/premieres/' + id + '?city_id=' + city_id)
