import pytest
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


def extract_value(element):
    for sup in element.find_all('sup'):
        sup.decompose()
    return element.text.strip()


def check_popularity(website, min_popularity):
    popularity_numeric = int(''.join(filter(str.isdigit, website.popularity)))
    return popularity_numeric >= min_popularity


@dataclass
class Website:
    name: str
    popularity: str
    front_end: str
    back_end: str
    database: str
    notes: str


url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"class": "wikitable"})
websites = []

for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")
    name = extract_value(columns[0])
    popularity = extract_value(columns[1])
    front_end = extract_value(columns[2])
    back_end = extract_value(columns[3])
    database = extract_value(columns[4])
    notes = extract_value(columns[5])

    websites.append(Website(name, popularity, front_end, back_end, database, notes))


@pytest.mark.parametrize("min_popularity",
                         [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
def test_popularity_check(min_popularity):
    for website in websites:
        assert check_popularity(website, min_popularity), (
            f"{website.name} "
            f"(Frontend:{website.front_end}|Backend:{website.back_end}) "
            f"has {website.popularity} unique visitors per month. "
            f"(Expected more than {min_popularity})"
        )
