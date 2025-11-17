#!/usr/bin/env python3

import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Unealtă pentru a obține definiții la cuvinte direct în terminal")
parser.add_argument("word", help="Cuvântul pe care vrei să-l cauți")
args  = parser.parse_args()

def make_request(word=""):
    # Make a GET request to a URL
    response = requests.get(f'https://www.dexonline.ro/definitie/{word}')
    
    # Check the status code
    # print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        print(f"Cod de la request greșit: {response.status_code}")
        exit()
    return response.text

page_text = make_request(args.word)
soup = BeautifulSoup(page_text, 'html.parser')

main_defs = soup.select('li.type-meaning.depth-0 > div.meaningContainer > div.meaning-row > span.tree-def.html')

if not main_defs:
    print("Nu au fost găsite definiții principale")
else:
    for i, definition in enumerate(main_defs, start=1):
        print(f"{i}. {definition.get_text(strip=True)}")

