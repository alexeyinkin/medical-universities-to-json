# universities-to-json

This script parses medical schools from https://search.wdoms.org

1. Download the HTML using:
```bash
python3 download.py
```

This will create `downloaded/` directory and many HTML files in it. Each file is a page result. There are separate page sets from open schools and closed schools because unfiltered requests are not allowed. The number of pages for both open and closed schools are hardcoded in `download.py`. Check if they need to be increased before running.

2. Convert HTML files to JSON using:
```bash
python3 html-to-json.py --entities=universities > universities.json
python3 html-to-json.py --entities=countries > countries.json
python3 html-to-json.py --entities=cities > cities.json
```

This will run through every file in `downloaded/` and produce a joined JSONs.

## Firebase Import
In case you want to import this JSON to Firebase, use this:

```bash
npm install -g node-firestore-import-export
firestore-import --accountCredentials credentials.json --backupFile universities.json --nodePath universities
```

where `credentials.json` is a file you export from Firebase console as per this tutorial: https://www.youtube.com/watch?v=gPzs6t3tQak
