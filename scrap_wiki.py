import re
import requests
from bs4 import BeautifulSoup


target_webpage_link = "https://id.wikipedia.org/wiki/Surah"

target_webpage = requests.get(target_webpage_link)

soup = BeautifulSoup(target_webpage.text, "html.parser")

def scrap_table():
    table = soup.find("table", class_="wikitable")
    rows = table.find_all("tr")[1:] # Skip first row

    Quran_data = []
    for row in rows:
        column = row.find_all("td")
        surah_index = column[0].text.strip()
        surah_name = column[1].text.split("Surah")[1].strip()
        number_of_verses = column[4].text.strip()
        Quran_data.append(f'{surah_index},{surah_name},{number_of_verses}')

    convert_to_csv = "\n".join(Quran_data)
    return convert_to_csv

with open("Quran Data.csv", "w") as file:
    file.write(scrap_table())
