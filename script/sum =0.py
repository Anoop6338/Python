

p=[]
#count = 0
for i in range(50,200+1):
	count=0
	for j in range(2,(i//2)+1):
		if i%j==0:
			count = count+1
			break
	if count==0:
		p.append(i)
sum = 0
for k in range(0,len(p)):
	sum=sum+p[k]
print(sum)
print(p)