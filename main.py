import requests
from datetime import datetime
from pprint import pprint

def search_tag(days, tag):
    #Расчет дат начала и окончания для диапазона поиска:
    final_date = int(datetime.timestamp(datetime.now()))
    initial_date = final_date - days*60*60*24

    #Заполнение словаря параметров:
    params = {'previous_day': initial_date, 'the_next_day': final_date, 'tagged': tag, 'site': 'stackoverflow'}

    resp = requests.get('https://api.stackexchange.com/2.3/questions', params=params)
    print('Вопросы, заданные в течении последних 2х дней, с тегом "Python":')
    for question in resp.json().get('items'):
        print(question['title'])

if __name__ == '__main__':
    search_tag(2, 'python')