with open('dataset_24465_4.txt','r') as df:
    info = df.readlines()

info.reverse()

with open('results.txt', 'w') as rf:
    rf.writelines(info)

