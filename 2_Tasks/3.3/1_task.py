import requests, re

temp_res = []


def url_checker(url, url_d):
    request = requests.get(url)
    temp2 = re.search(patternURL, request.text)
    if temp2.group() == url_d:
        temp_res.append('Yes')
    else:
        temp_res.append('No')
    return temp_res


patternURL = r'(http*.*html)'
url_p = input().strip()
url_d = input().strip()
req = requests.get(url_p)
temp = re.findall(patternURL, req.text)

for value in temp:
    result = url_checker(value, url_d)

print('Yes' if 'Yes' in temp_res else 'No')