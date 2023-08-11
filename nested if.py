# a,b,c= 10,20,30

# if a<b :
#     if a>c:
#         print ("a is max :",a)

# elif b<c:
#     print("b is max:", b)

# else :
#     print("c is max:",c)

for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")
print("----------------")

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
print("----------------")

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")
