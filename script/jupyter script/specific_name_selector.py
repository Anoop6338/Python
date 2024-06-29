list_1 = ["sheep", "teep", "ram", "sohan"]
msg = "y"
while msg:
    names= input("enter names:")
    list_1.append(names)
    ques=input("add more names")
    if msg!=ques:
        break
print("names stored succesfully")
for i in list_1:
    if "eep" in i:
        print(i)
        

    
