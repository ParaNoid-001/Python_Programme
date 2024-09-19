x=0
while not(1<=x<=100):
    x=int(input("Enter a number between 1 and 100 : "))
    print("valid no", x)

#for loop

for i in range(4):
    x=int(input("\nEnter your number : "))
    if (1<=x<=100):
        print("valid no",x)
        break
    else:
        print("Invalid No")

#to check if a number is armstrong or not

num=(input("\nEnter your number : "))
length=len(str(num))
sum=0
for i in num:
    sum=sum+int(i)**length
if (sum==int(num)):
    print("The given number",num,"is an Armstrong number")
else:
    print("Not an Armstrong number")

#to check if a number is armstrong or not using WHILE LOOP

num1=int(input("Enter your Number : "))
length1=len(str(num1))
temp=num1
sum=0
while(temp>0):
    r=temp%10
    sum=sum+r**length1
    temp//=10
if (sum==num1):
    print("The given number",num,"is an Armstrong number")
else:
    print("Not an Armstrong number")

