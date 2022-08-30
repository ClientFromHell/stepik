import zipfile
import glob

zip = zipfile.ZipFile('main.zip')
zip.extractall()
zip.close()

filePattern = r'main/**/*.py'
path = glob.glob(filePattern, recursive=True)

for i in range(len(path)):
    if path[i].endswith('.py'):
        path[i] = path[i][:-9]

path = sorted(list(set(path)))

with open('answers.txt', 'w') as file:
    for _ in path:
        file.write(f'{_}\n')
