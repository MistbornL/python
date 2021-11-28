from bs4 import BeautifulSoup
import requests

from typing import List


def parser(info: List):
    # parse multiple pages
    for page in range(1, 36):
        url = f'https://ss.ge/ka/udzravi-qoneba/l/bina?Page={str(page)}&RealEstateTypeId=5&MunicipalityId=95' \
              f'&CityIdList=95&subdistr=44&PrcSource=1&StatusField%27%20\%20%20%20%20%20%20%27.FieldId=34&StatusField' \
              f'.Type=SingleSelect&StatusField.StandardField=Status&QuantityFrom=90&PriceType=false%27%20\%20%20%20' \
              f'%20%20%20%27&CurrencyId=1 '
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')
        # find data frame
        frame = soup.find_all('div', class_="latest_article_each")

        # get specific data
        try:
            for item in frame:
                title = item.find('span', class_="TiTleSpanList").text.strip()
                location = item.find('div', class_="StreeTaddressList").text.strip()
                km = item.find('div', class_="latest_flat_km").text.strip()
                flat = item.find('div', class_="latest_flat_type").text.strip()
                stair = item.find('div', class_="latest_stair_count").text.strip()
                price = item.find('div', class_="latest_price").text.strip()

                info.append(f'{title},{location},{km},{flat}, {stair},{price}')
        except AttributeError:
            "no info"
