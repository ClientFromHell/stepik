import requests, re

results = []
urls_on_first_page = []
patternURL = r'(http*.*html)'
# url_p = input().strip()
# url_d = input().strip()
url_p = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
url_d = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'

req = requests.get(url_p)
if req.status_code == 200:
    temp = re.findall(patternURL, req.text)
    for link in urls_on_first_page:
        req = requests.get(link)
        if req.status_code == 200 and:

print(urls_on_first_page)


