# def container():
#     n=int(input("enter a number"))
#     con=[]
#     for i in range(n):
#         value=input("enter the value")
#         con.append(value)

    
#     return con

# a=container()
# print (a)

# d=container()
# print ("d in value :",d)

# def add():
#     a=int(input("enter a number :"))
#     b=int(input("enter a number :"))

#     return a+b

# print("your answer :",add())

# def add():
#     a=int(input("enter a number :"))
#     b=int(input("enter a number :"))
#     c=a+b
#     return c
# print("your answer",add())

# recursive function
# 1 * 2 * 3 * 4 * 5=120

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x - 1))
 
 
# print("Factorial : ", factorial(5))

"""
factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1
120
"""
# def add(a, b):
#     c = a + b
#     print("value of: ", c)
 
 
# add(25, 2)
    
def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a * b
    return c
 
 
x=mul()
print("Mul ",x)

def add(a, b):
    c = a + b
    return c
 
 
x = add(25, 2)
print("add is ", x)