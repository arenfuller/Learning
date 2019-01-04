import math
#Input dimensions of room
length=float(input("enter length of room"))
Height=float(input ("enter height of wall"))
#Input width of room
Width=float(input("Enter width of room"))
#Input Size of door
Wdoor=float(input ("Enter width of door"))
Hdoor=float(input("enter height of door"))
#Calculate area of door
Darea=Wdoor*Hdoor
#Calculate Area of Walls
L1=length*Height
W1=Width*Height
Area=(L1*2)+(W1*2)-Darea
#Calculate coverage of paint taking that one tin covers 3m square
Tins=Area/3
FTins=round(Tins)

CCan=float(input("enter price per can of paint"))
TCost=CCan*Tins
math.ceil(TCost)

print (f"you will need {FTins} of tins to paint your walls")
print (f"It will cost £{TCost}")  

