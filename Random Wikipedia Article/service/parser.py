from bs4 import BeautifulSoup
import requests


def parse_material():
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, 'html.parser')
    title = soup.find("h1", _class="firstHeading mw-first-heading").text
    print(title)
