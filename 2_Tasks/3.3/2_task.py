import re, requests

link = input()
r = requests.get(link).text

with open('url_file.txt', 'w') as file:
    file.write(r)

res_upd = []
pattern = r'<a.*href=[\'\"][^ftp\._\-][http|https://]*[\w]*[-|\w]*\.[-\w.]*'
pattern2 = r'[^://|\'\"]*[\w]*$'
with open('url_file.txt', 'r') as file:
    lines = file.readlines()
    lines = "".join(lines).strip()

result = re.findall(pattern, lines)

results = []
for i in result:
    value = re.findall(pattern2, i)
    results.append(value)

end = []
for i in results:
    end.append(i[0])

print(*sorted(list(set(end))), sep='\n')
