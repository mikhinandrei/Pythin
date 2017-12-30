from lxml.html import fromstring
from lxml.etree import XMLSyntaxError

from urllib.request import urlopen
from urllib.parse import urljoin

import re

import pandas as pd

YEAR = '2016-2017'
URL = 'http://winter.sport-express.ru/biathlon/worldcup/' + YEAR + '/ratings/'
DET_PATH = '.container .grid_3 .winter_box .bounding_box .ml_10 .w_480 .se_score'
TOWN_PATH = '.container .grid_3 .winter_box .bounding_box .ml_10 .w_480 .se_score .gray_block'
N = 71

names = []
countries = []
sum_points = []
best_place = []
best_type = []
best_city = []

def parse_wc(number):
    site = urlopen(URL)
    html = site.read().decode('windows-1251')
    list_doc = fromstring(html)

    tr = list_doc.cssselect('tr')[1:number]

    sportsmen =[]

    for elem in tr:
        td = elem.cssselect('td')[1]

        name = td.cssselect('a')[0].text.upper().rstrip().lstrip()

        href = td.cssselect('a')[0].get('href')

        url = urljoin(URL, href)
        url = urljoin(url, YEAR)
        details = urlopen(url).read().decode('windows-1251')
        try:
            details_doc = fromstring(details)
        except XMLSyntaxError:
            continue


        best = 99
        for line in details_doc.cssselect(DET_PATH):
            table = line.cssselect('table')
            for k in table:
                towns = details_doc.cssselect(TOWN_PATH)
                info = k.cssselect('tr')
                title = info[0]
                cup = str(title.cssselect('th')[0].text)
                if 'мира' not in cup.lower():
                    continue
                for item in info:
                    if item in towns:
                        t = item.cssselect('td')[1]
                        town = t.cssselect('b')[0].text
                    try:
                        call = item.cssselect('td')[2]
                        event = str(call.cssselect('a')[0].text)
                        if 'эстафета' in event.lower():
                            continue
                        place = int(item.cssselect('td')[3].text)
                        if place <= best:
                            best = place
                            run = event
                            city = town
                    except IndexError:
                        continue


        country = elem.cssselect('td')[3].text  # comment
        points = elem.cssselect('td')[4].text

#        sportsman = {'name': name, 'country': country, 'points': points, 'best': best, 'run': run, 'city': city}
        names.append(name)
        countries.append(country)
        sum_points.append(points)
        best_place.append(best)
        best_type.append(run)
        best_city.append(city)
 #       sportsmen.append(sportsman)

    return sportsmen


def main():
    sportsmen = parse_wc(N)
    #for item in sportsmen:
    #    print(item['name'], ' ', item['country'], ' ', item['points'], '  Лучший результат:', item['best'], ' место ', item['run'], item['city'])
    table = pd.DataFrame({
        'Имя': names,
        'Страна': countries,
        'Баллы': sum_points,
        'Место': best_place,
        'Тип гонки': best_type,
        'Город': best_city
    }, index=range(1, N))
    table.to_csv('report_' + YEAR + '.csv')


if __name__ == '__main__':
    main()
