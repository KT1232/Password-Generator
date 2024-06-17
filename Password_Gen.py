import random
length = int(input("Please input the desired length for your password." "\n"))
password = ""
specialChars = ["%", "$", "&", "*", "!", "?", "#", "@"]
for i in range(length):
    f = random.random()
    if f > .6:
        g = random.randint(65,90)
        password +=(chr(g))
    elif f <.4:
        g = random.randint(97,123)
        password +=(chr(g))
    else:
        g = random.randint(0,7)
        password +=(specialChars[g])
print(password)