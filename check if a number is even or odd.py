num = int(input("Enter a number: "))
def is_even(num):
    return num % 2 == 0

if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")

