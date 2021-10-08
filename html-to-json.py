import json
from os import listdir
from os.path import isfile, join
from pathlib import Path
import re

dir_ = 'downloaded'
files = [f for f in listdir(dir_) if isfile(join(dir_, f))]

dict = {}

rowStart = '<tr style="cursor: pointer">'
rowEnd = '</tr>'
rowContentRegExp = re.compile('<td.*>(\\d+)</td>.*<td>(.*)</td>.*<td><a.*>(.*)</a>.*</td>.*<td>(.*)</td>')

for filename in files:
    path = dir_ + '/' + filename

    content = Path(path).read_text().replace('\n', '')
    start = 0

    while start != -1:
        start = content.find(rowStart, start + 1)
        end = content.find(rowEnd, start)
        row = content[start + len(rowStart) : end]

        match = rowContentRegExp.search(row)
        if match == None: continue # TODO: Log error

        id      = match.group(1)
        country = match.group(2)
        title   = match.group(3)
        city    = match.group(4)

        dict[id] = {
            'country':  country,
            'title':    title,
            'city':     city,
        }

print(json.dumps(dict))
