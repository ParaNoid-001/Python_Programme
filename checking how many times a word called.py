
#str = "AVHGF567832873kjfdj"
str = input ("Enter your string: ")
dict = {}

for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for i in dict:
    print(f"{i} = {dict[i]}")
