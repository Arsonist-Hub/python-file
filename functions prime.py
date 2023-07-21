def container():
    n=int(input("eneter a number"))

    flag=False
    if n>2:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                flag = True
    if flag:
        return n,"is not prime number"

    else:
        return n,"is prime number"

a = container()
print(a)

    
