#runtime error handling
try: 
    num1=int(input("enter your 1st number:"))
    num2=int(input("enter your 2nd number:"))
    result=num1/num2
    print(num1, "divided by", num2, "is", result)

except ZeroDivisionError:
    print("cannot divide by zero, try again.")

except ValueError:
    print("Both inputs must be numbers, sorry. ")
    
