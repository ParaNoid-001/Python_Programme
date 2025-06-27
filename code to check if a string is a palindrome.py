# str= input("Enter a string: ")

# rev_str= str[::-1]
# if rev_str ==str:
#     print(f"{str} is a palindrome")

str = input("Enter a string: ")

def is_palindrome(str):
    return str == str[::-1]

if is_palindrome(str):
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")