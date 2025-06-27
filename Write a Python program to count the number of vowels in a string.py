text = input("Enter a string:")
count = 0
vowel = ""
vowels = "aeiouAEIOU"

for i in text:
    if i in vowels:
        count += 1
        vowel += i
print ("number of vowels: ", count)
print ("vowels are : " ,vowel)
