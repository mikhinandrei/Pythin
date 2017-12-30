from lxml.html import fromstring
from lxml.etree import XMLSyntaxError

from urllib.request import urlopen
from urllib.parse import urljoin


URL = 'https://en.wikipedia.org/wiki/'
CAPITAL_PATH = ' .MW-BODY-CONTENT .MW-CONTENT-LTR .INFOBOX '

def parse(country):
    url = urljoin(URL, country)
    site = urlopen(url)
    html = site.read().decode('utf-8')
    list_doc = fromstring(html)

    tr = list_doc.cssselect('tr')
    print(tr)
    i = tr[6]
    td = i.cssselect('td')
    capital = td[1]
    span = capital.cssselect('a')
    capital = span[0].text
    print(capital)

def main():
    #country = input().lower()
    parse('Russia')

if __name__ == '__main__':
    main()