#Exam Marks input
#for this to work they must be outside the validation rules e.g. not between 0-100
RawMark1=-1
RawMark2=-1

while RawMark1 <0 or RawMark1 >100:
    RawMark1=int(input("Enter delegates raw score for paper 1:"))
    
    if RawMark1 <0 or RawMark1 >100:
        print ("Score is invalid, check and try again")
        
while RawMark2 <0 or RawMark2 >100:
    
    RawMark2=int(input("Enter delegates raw score for paper 2:"))
    if RawMark2 <0 or RawMark2 >100:
        print ("Score is invalid, check and try again") 


#Average of grades
AverageGrade=float(RawMark1+RawMark2)/2


#AssigningGrades
if AverageGrade <40:
   print ("Fail")


elif AverageGrade <65:
    print ("Pass")


elif AverageGrade >85:
    print ("Merit")

else:
    print ("Distinction")
