def sum():
  L=[]
  msg= "y"
  while msg=="y":
    entry=int(input("enter your number"))
    L.append(entry)
    ques=input("wanna add more:")
    if msg!=ques:
      break
  numsum=0
  for i in L:
    numsum +=i
  print(numsum)
  L.sort()
  print(L)
