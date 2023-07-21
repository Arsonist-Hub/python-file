n= int(input("enter a value"))

def even1 (m):
       print("witth argument and return")
       print("running even1() function")

       if m%2==0:
          return"even"

       else:
             return"odd"

result1 = even1(n)
print(result1)

def even2():

     print("without Arguments and return type")
     print("running even2() function")

     n = int(input("enter a number"))
     if n%2==0:
          print("even")

     else:
          print('odd')

even2()

def even3(n):

    print("with argument and without return")
    print("running even() function")

    if n % 2 == 0:
        print("even")

    else:
        print("odd")


even3(2)


def even4():
    print("without argument and with return type")
    print("running even4() function")

    n=int(input("enter a number"))

    if n%2==0:
           return "even"
    else:
       return "odd"     

result2=even4()
print(result2) 
    




                        