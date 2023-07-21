n=int(input("enter: "))

flag=False

if n>2:
    for i in range(2,int(n/2)+1):
        if n%i==0:
            flag=True

if flag:
    print (n,": is composite no")

else:
    print(n,": is prime no")
            