#slicing example
mystring= "Hello World"
print("1st character", mystring[0])
print("5th character", mystring[4])
print("last character by position", mystring[10])
print("always the last character", mystring[-1])
print("first 3 characters", mystring[:3])
print ("a slice of the string", mystring[2:6])
print ("a slice of the string incrementally", mystring[2:6:2]) #starts at 2 and goes to 6 in increments of 2 
print ("string reveresed", mystring[::-1]) 
#slicing can be used on other data containers, not just strings 
#1st character H
#5th character o
#last character by position d
#always the last character d
#first 3 characters Hel  note that the [:3] means unspecified to three and it defaults to the first [0:3] could be done too
#a slice of the string llo 
#a slice of the string incrementally lo
#string reveresed dlroW olleH

#challenge 2 I want the result drWoldH
print("Challenge Result", mystring[-1::-2])


