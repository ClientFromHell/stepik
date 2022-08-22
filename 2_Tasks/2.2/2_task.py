from simplecrypt import decrypt, DecryptionException

with open("encrypted.bin", "rb") as file:
    encrypted = file.read()


with open("passwords.txt","r") as pwd:
    lines = pwd.readlines()

c = 0

for i in lines:
    c += 1
    try:
        print('\nDecrypted password is: ', decrypt(i[:-1], encrypted).decode('utf-8'), '\n')
    except DecryptionException:
        print(f'{i[:-1]} - Not correct result')


print(f'{c} passwords have been checked')


