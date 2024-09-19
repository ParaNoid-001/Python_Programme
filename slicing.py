string1="Gate SMashers"
substr1=string1[1:4]
print(substr1)
substr2=string1[::-1]
print(substr2)
substr3=string1[5::2]
print(substr3)
substr4=string1[5:12].upper()
print(substr4)

print(string1.title())
print(string1.lower())

str1='Hello, world!'
print(str1.endswith('World!'))
print(str1.startswith('Hello'))
print(str1.istitle())
print(str1.replace('o','*'))
print(str1.replace('world!','country'))
