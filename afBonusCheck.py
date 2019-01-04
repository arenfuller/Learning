#Dictionary of comapny bonus schemes
GradeBonus={'1':0.01, '2':0.02, '3':0.035}

#Ask the user their annual salary and their grade
Salary=float(input ("Enter your annual salary £"))
Grade= input ("Enter your grade ")
Bonus=Salary*GradeBonus[Grade]
print("your bonus this year is £", Bonus)
print("Your annual salary including bonus is £", Bonus+Salary)
