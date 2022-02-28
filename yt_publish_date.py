import sys
from datetime import datetime as dt

import requests
from lxml import html

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}


def get_doc(url: str, **kwargs):
    response = requests.get(url, **kwargs)
    if not response:
        return print(f'Failed to get {url}')
    return html.fromstring(response.text)


def extract_publish_date(doc):
    result = doc.xpath('//meta[@itemprop="datePublished"]/@content')
    return dt.fromisoformat(result[0]).strftime('%d.%m.%Y') if result is not None else None


def main(url: str):
    doc = get_doc(url, headers=HEADERS)
    if doc is None:
        return
    pub_date = extract_publish_date(doc)
    return print(f'Дата публикации: {pub_date if pub_date else "Не найдена"}')


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else input('Введите URL: ')
    main(url)
