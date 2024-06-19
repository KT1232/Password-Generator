import random
length = int(input("Please input the desired length for your password." "\n"))
password = ""
specialChars = ["%", "$", "&", "*", "!", "?", "#", "@"]
for i in range(length):
    f = random.random()
    if f > .7:
        g = random.randint(65,90)
        password +=(chr(g))
    elif f <.3:
        g = random.randint(97,123)
        password +=(chr(g))
    elif f >= .3 and f < .5:
        g = random.randint(0,7)
        password +=(specialChars[g])
    else:
        g = random.randint(48,57)
        password +=(chr(g))
print(password)