import requests, re

results = []
urls_on_first_page = []
patternURL = r'(http*.*html)'
url_p = input().strip()
url_d = input().strip()


def urlstatuschecker(url):
    return True if url.status_code == 200 else False


req = requests.get(url_p)

if urlstatuschecker(req):
    urls_on_first_page = re.findall(patternURL, req.text)

for link in urls_on_first_page:
    req = requests.get(link)
    if urlstatuschecker(req):
        results.extend(re.findall(patternURL, req.text))

if url_d in results:
    print('Yes')
else:
    print('No')
