from urllib.request import urlopen
from urllib.parse import urljoin

from lxml.html import fromstring
from lxml.etree import XMLSyntaxError
from xlsxwriter import *

URL = 'http://proglive.ru/courses'
ITEM_PATH = '.our-courses_list .our-courses_item .right'
DESCR_PATH = '.section-info .left-sect'
TEACH_PATH = '#teach_slider .reader_desc .name'

def parse_courses():
    f = urlopen(URL)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)

    courses = []

    for elem in list_doc.cssselect(ITEM_PATH):
        a = elem.cssselect('a')[0]
        href = a.get('href')
        name = a.text
        p = elem.cssselect('p')[0]
        lead = p.text
        url = urljoin(URL, href)

        course = {'name': name, 'lead': lead, 'url': url}
        details_html = urlopen(url).read().decode('utf-8')

        try:
            details_doc = fromstring(details_html)
        except XMLSyntaxError:
            continue

        descr_elem = details_doc.cssselect(DESCR_PATH)[0]
        descr = descr_elem.text_content()

        teach_elem = details_doc.cssselect(TEACH_PATH)
        teachers = [teacher.text for teacher in teach_elem]

        #course['descr'] = descr
        course['teacher'] = teachers

        courses.append(course)
    return courses


def export_excel(filename, courses):
    pass

def main():
    courses = parse_courses()
    export_excel('courses.xlsx', courses)

if __name__ == '__main__':
    main()
