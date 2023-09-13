import random

parol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
rap = int(input('введи длину пароля '))
password = ''

for i in range(rap):
    password += random.choice(parol)
print(password)
