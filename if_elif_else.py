#if,elif,else & nested

#if:
age=int(input("Enter your age : "))
if age>=18:
    print("Adult")
else:
    print("Minor")

#elif:
x=12
z=0
if x>0:
    print("x is a positive number")
elif x==0:
    print("x is 0")
else:
    print("x is a negative number")

#elif:

# Ask the user for input
user_input = input("Enter a number between 1 and 7: ")
number = int(user_input)
    
if number == 1:
    day = "Sunday"
elif number == 2:
    day = "Monday"
elif number == 3:
    day = "Tuesday"
elif number == 4:
    day = "Wednesday"
elif number == 5:
    day = "Thursday"
elif number == 6:
    day = "Friday"
elif number == 7:
    day = "Saturday"
else:
    day = "Invalid number. Please enter a number between 1 and 7."
print(day)
