num = int(input("Enter your number: "))
prime_num=[]



def isprime(num):
    for j in range(2,(num//2)+1):
        if num%j==0:
            print("Number entered is not a prime number!!")
            break
    else:
        print("Number entered is a prime number!!")



def next_prime(num):
    i=1    
    while len(prime_num)<5:
        count=0
        prev_num = num-i
        for k in range (2,(prev_num//2)+1):
            if prev_num%k==0:
                count=1
                break
        if count==0:
            b= prev_num
            prime_num.append(b)
            i=i+1   
        else:
            i=i+1



    i=1
    while len(prime_num)<10:
        count=0
        next_num = num+i        
        for k in range (2,(next_num//2)+1):
            if next_num%k==0:
                count=1
                break
        if count==0:
            a= next_num
            prime_num.append(a)
            i=i+1       
        else:
            i=i+1

    prime_num.sort()
    print(*prime_num, sep = ", ")
   
     
isprime(num)
next_prime(num)
