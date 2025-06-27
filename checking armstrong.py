num = int(input("Enter a number: "))
temp = num

#count = 0
# Count the number of digits
# while temp > 0:
#     temp = temp // 10
#     count += 1

length = len(str(num))

# Reset temp and calculate sum of digits raised to power of count
temp = num
result = 0
while temp > 0:
    digit = temp % 10
    result += digit ** length
    temp = temp // 10

# Check and print result
if result == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
