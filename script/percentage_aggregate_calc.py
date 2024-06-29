sub1 = int(input("enter subject1 marks: "))
sub2 = int(input("enter subject2 marks: "))
sub3 = int(input("enter subject3 marks: "))
sub4 = int(input("enter subject4 marks: "))
sub5 = int(input("enter subject5 marks: "))

aggregate1 = sub1*100/100
if aggregate1<=100:
    print("Aggregate marks in subject1 is:",aggregate1,"%")
else:
    print("write subject marks less than 100")

aggregate2 = sub2*100/100
if aggregate2<=100:
    print("Aggregate marks in subject2 is:",aggregate2,"%")
else:
    print("write subject marks less than 100")

aggregate3 = sub3*100/100
if aggregate3<=100:
    print("Aggregate marks in subject3 is:",aggregate3,"%")
else:
    print("write subject marks less than 100")

aggregate4 = sub4*100/100
if aggregate4<=100:
    print("Aggregate marks in subject4 is:",aggregate4,"%")
else:
    print("write subject marks less than 100")

aggregate5 = sub5*100/100
if aggregate5<=100:
    print("Aggregate marks in subject5 is:",aggregate5,"%")
else:
    print("write subject marks less than 100")


percent = (sub1 + sub2 + sub3 + sub4 + sub5)/5
if percent<=100:
    print("Your pencentage =",percent,"%")

else:
    print("you have written one of the subject marks more than 100")

