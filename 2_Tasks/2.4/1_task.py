with open('dataset_24465_4.txt','r') as df, open('results.txt', 'w') as rf:
    info = df.readlines()
    info.reverse()
    rf.writelines(info)


