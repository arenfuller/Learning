#Engine size of 1.3L or larger are awarded 23p per mile
#those unser 1.3L are awarded 15p per mile

ExpensiveMile="23p"
CheapMile="15p"


#UserInput for engine size
EngineSize=float(input("Input your engine size"))

#User input for milage
Milage=float(input("Enter the total mileage travelled"))

if EngineSize >= 1.3:
    AmountGranted1=Milage*23
    print("your claim is " ,AmountGranted1)

else:
    AmountGranted2=Milage*15
    print("your claim is ", AmountGranted2)
    
    
