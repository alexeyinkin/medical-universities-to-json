import subprocess
from pathlib import Path

# Check if these are still valid:
openPageCount = 178
closedPageCount = 10

curlBashParts = [
    'curl',
    'https://search.wdoms.org/',
    '-H', 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
    '-H', 'Accept: */*',
    '-H', 'Accept-Language: en-US,en;q=0.5',
    '--compressed',
    '-H', 'Referer: https://search.wdoms.org/',
    '-H', 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
    '-H', 'X-Requested-With: XMLHttpRequest',
    '-H', 'Origin: https://search.wdoms.org',
    '-H', 'Connection: keep-alive',
    '-H', 'Cookie: _ga=GA1.2.169048152.1633535789; _gid=GA1.2.941711511.1633698037',
    '-H', 'Sec-Fetch-Dest: empty',
    '-H', 'Sec-Fetch-Mode: no-cors',
    '-H', 'Sec-Fetch-Site: same-origin',
    '-H', 'Pragma: no-cache',
    '-H', 'Cache-Control: no-cache',
    '--data-raw',
]
openDataTemplate = 'sCountryName=&sSchoolName=&sCityName=&sOperationFlag=Y&iPageNumber=__PAGE__&UN_MemberStatus=&sessionId='
closedDataTemplate = 'sCountryName=&sSchoolName=&sCityName=&sOperationFlag=N&iPageNumber=__PAGE__&UN_MemberStatus=&sessionId='

pagePlaceholder = '__PAGE__'

Path('downloaded').mkdir(parents=True, exist_ok=True)

for page in range(1, openPageCount + 1):
    print('Downloading Open Page ' + str(page));

    curlData = openDataTemplate.replace(pagePlaceholder, str(page));
    pageCurlParts = curlBashParts + [curlData];

    content = subprocess.check_output(
        pageCurlParts,
    )

    with open('downloaded/open_' + str(page) + '.html', 'wb') as f:
        f.write(content)

for page in range(1, closedPageCount + 1):
    print('Downloading Closed Page ' + str(page));

    curlData = closedDataTemplate.replace(pagePlaceholder, str(page));
    pageCurlParts = curlBashParts + [curlData];

    content = subprocess.check_output(
        pageCurlParts,
    )

    with open('downloaded/closed_' + str(page) + '.html', 'wb') as f:
        f.write(content)
