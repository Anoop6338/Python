num=int(input("enter your number?"))
if num!=0:
    if num!=1:
        if num>=2:
            for i in range(2,num-1):
                if (num%i)==0:
                    prime=0
                    print("it's not a prime number")
                    break
                else:
                    prime=1
            if prime==1:
                print('its a prime number')
        else:
            print('its a prime number')
    else:
        print('neither composite nor prime')
else:
    print('invalid')


