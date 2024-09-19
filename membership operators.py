#membership operators 'in'

reg_user=[ "varun","amit","sahil"]
name=input("Enter your name: ")
if name in reg_user:
    print("access granted")
else:
    print("acess denied")
