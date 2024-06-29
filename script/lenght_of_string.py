str1= input("enter your string")

print("using direct function", len(str1))


length=0
for i in str1:
    length +=1
print("using for loop", length)



leng=0
while str1[leng:]:
    leng +=1
    
print("using while loop", leng)







