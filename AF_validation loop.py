###adding a loop for validation

age=0

while age <18 or age > 120:
    age=int (input("enter your age(18-120):"))
    if age <18 or age > 120:
        print ("age is invalid, please try again.") 

