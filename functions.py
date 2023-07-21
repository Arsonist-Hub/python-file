def container():
    n=int(input("enter a number"))
    con=[]
    for i in range(n):
        value=input("enter the value")
        con.append(value)

    
    return con

# a=container()
# print (a)

d=container()
print ("d in value :",d)
