import argparse
import html
import json
from os import listdir
from os.path import isfile, join
from pathlib import Path
import re

def fill_universities(content, dict):
    start = 0

    while start != -1:
        start = content.find(rowStart, start + 1)
        end = content.find(rowEnd, start)
        row = content[start + len(rowStart) : end]

        match = rowContentRegExp.search(row)
        if match == None: continue # TODO: Log error

        id      = match.group(1)
        country = html.unescape(match.group(2))
        title   = html.unescape(match.group(3))
        city    = html.unescape(match.group(4))

        dict[id] = {
            'countryTitle': country,
            'title':        title,
            'cityTitle':    city,
        }

def fill_countries(content, dict):
    universities = {}
    fill_universities(content, universities)

    for id in universities:
        university = universities[id]
        countryTitle = university['countryTitle']

        dict[countryTitle] = {
            'title': countryTitle,
        }

def fill_cities(content, dict):
    universities = {}
    fill_universities(content, universities)

    for id in universities:
        university = universities[id]
        countryTitle = university['countryTitle']
        cityTitle = university['cityTitle']

        dict[cityTitle] = {
            'countryTitle': countryTitle,
            'title':        cityTitle,
        }


parser = argparse.ArgumentParser(description='Parses universities from HTML.')
parser.add_argument('--entities', metavar='ENTITIES', type=str, help='universities | countries | cities')

args = parser.parse_args()

entities = args.entities

if not entities in ['universities', 'countries', 'cities']:
    raise ValueError('Invalid value for entities')

dir_ = 'downloaded'
files = [f for f in listdir(dir_) if isfile(join(dir_, f))]

dict = {}

rowStart = '<tr style="cursor: pointer">'
rowEnd = '</tr>'
rowContentRegExp = re.compile('<td.*>(\\d+)</td>.*<td>(.*)</td>.*<td><a.*>(.*)</a>.*</td>.*<td>(.*)</td>')

for filename in files:
    path = dir_ + '/' + filename

    content = Path(path).read_text().replace('\n', '')

    if entities == 'universities':
        fill_universities(content, dict)
    elif entities == 'countries':
        fill_countries(content, dict)
    elif entities == 'cities':
        fill_cities(content, dict)

print(json.dumps(dict))
