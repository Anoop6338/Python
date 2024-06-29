str1=input("enter your string - ")
print(str1)
na=input("enter the word you want to search - ")
print(na in str1)
num=str1.count(na)
print(num)
i=int(num)
#while i in num:
#    result=str.index(na)
#    print(result,result)
#    i-=1()
my_dict = dict()
for x in str1:
    if x in my_dict:
        my_dict[x] = my_dict[x] + 1
    else:
        my_dict[x] = 1

print(my_dict[na])
