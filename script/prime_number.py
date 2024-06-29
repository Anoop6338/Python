num=int(input("enter your number"))
for num in range(2,num+1):
    for i in range(2,num):
        if (num%i)==0:
            break
        #here break helps to diffrentiate if from else 
    else:
        #to print numbers in different columns remove end=","
        print(num,end=",")