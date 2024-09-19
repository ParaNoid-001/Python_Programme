first_string='Hello, world!'
print("first_string")
print(len(first_string))
print(first_string[1])
if "txt" in first_string:
    print("yes, txt is available")
else:
    print("not, available")
print(first_string[1:4])

#the string2 is a integar so either we've to do type casting or put that value inside '(value'
string1='Hello'
string2='20'
string3=string1+' '+string2
print(string3)

first='swarna'
last='ghosh'
age='23'
print(f'my first name is {first}, last name is {last}, age is {age}')
#or
print('my first name is {}, last name is {}, age is {}'.format(first,last,age))
