import re
import requests
from bs4 import BeautifulSoup


target_webpage_link = "https://en.wikipedia.org/wiki/List_of_chapters_in_the_Quran"

target_webpage = requests.get(target_webpage_link)

soup = BeautifulSoup(target_webpage.text, "html.parser")

def scrap_table():
    table = soup.find("table")
    rows = table.find_all("tr")
    
    Quran_data = []
    for row in rows:
        column = row.find_all("td")
        if column == []:
            pass
        else:
            surah_index = column[0].text.strip()
            surah_name = re.search(r"^[^(\s]+", column[1].text).group()
            # RegEx expression used to better extract surah name only, excluding any subtitutes or translation
            number_of_verses = re.search(r"^\d+", column[4].text).group()
            # RegEx expression used to extract number of verses only
            Quran_data.append(f'{surah_index},{surah_name},{number_of_verses}')
        
    convert_to_csv = "\n".join(Quran_data)
    return convert_to_csv

file = open("Quran Data.csv", "w")
file.write(scrap_table())