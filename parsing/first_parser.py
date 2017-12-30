from urllib.request import urlopen

from lxml.html import fromstring
from lxml.etree import XMLSyntaxError


URL = 'http://www.finmarket.ru/currency/rates/'
ITEM_PATH = '.main .center_column .karramba'


def parse_value(id):
    course = None
    change = None

    site = urlopen(URL)
    html = site.read().decode('windows-1251')
    list_doc = fromstring(html)

    print(html)

    tr = list_doc.cssselect('tr')[2:]

    for elem in tr:
        td = elem.cssselect('td')[0]
        if (td.text == id):
            course = elem.cssselect('td')[3]
            change = elem.cssselect('td')[4]
            return course.text, change.text

    return course, change


def main():
    item_for_search = input('Введите валюту\n')
    search_id = item_for_search.upper()
    course, change = parse_value(search_id)
    if course:
        print('Курс ', item_for_search.upper(), ' равен', course, u' рублей  ', change, '\n')
    else:
        print('Такая валюта не найдена\n')

if __name__ == '__main__':
    main()