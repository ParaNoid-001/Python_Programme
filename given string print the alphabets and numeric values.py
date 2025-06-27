text = input("enter a string: ")
alphabets =""
numbers =""
for char in text:
    if char.isalpha():
        alphabets += char
    elif char.isdigit():
        numbers +=char

print ("Alphabets:", alphabets)
print ("Numbers:", numbers)
