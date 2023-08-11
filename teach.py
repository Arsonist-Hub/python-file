# data types
# int
# str
# float
# list
# tuples
# set
# dictionary
# boolean "true","fals"

# sample
# a=20
# b=30
# c=a+b
# print (c)
# print(type(c))

# int
# a=int(20)
# b=int(30)
# c=a+b
# print (c)
# print(type(c))

# str
# a="20"
# b="30"
# c=a+b
# print(c)
# print(type(c))

# float
# a=float(10.2)
# b=float(30.6)
# c=a+b
# print(c)
# print(type(c))

# list
# a=[1,"hi","hello",3.8]
# print (a)

# a.append("hello world")# add to last
# print(a)

# a.pop()#last one remove or particular index in parameter
# print(a)

# a.remove("hello") #list inside of particular perameter acess
# print(a)

# a.extend(["hello", 123])
# print(a)
#example
# fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# fruits.extend(cars)
# print (fruits)
#exdentes example
# name=input("your name")
# age=input("enter your age")
# dob = input("enter a  date")
# userlist=[]
# userlist.extend([name,age,dob])

# set
# s={"mani",123 }
# print (s)
# s.add(756)
# print (s)
# l=[45678,"boo boo"] 
# s.update(l)
# print (s)
# s.discard("mani")
# print (s)

#dictionary

# o={'id':35,'name':'mani','dep':'it'}
# print(o)
# print (o['id'])
# print (o.items())
# print (o.keys())
# print (o.values())
# o.pop('id')
# print(o)
# o['study']="bca"
# print (o)

#condition statement
# boolean "true","fals"
# #if
# name =input("enter your name")
# age =int(input("enter your age"))

# if age > 18:
#     print ("hello",name,"license is approved")

# elif age==18:
#     print ("hello",name,"your are waiting list")


# else :
#     print ("hello",name,"not approved")

# looping counting loop
# 1 for loop
# for i in range(0,10,3): #range (initial,final,step) i in counting auto increase
#     print(i)
# n = 20
# for i in range (1,n+1):
#     print (i)

#while loop  this loop in the condition satisfied of continues looping
# i=1
# while i<10:
#     print(i) #the line of run infinity loop
#     i = i+1 #manualy increace a counting

#jumping statement
#continue
# for i in range(0,10):
#     if i==6:
#         continue
#     print(i)
# #break
# for i in range(0,10):
#     if i==4+1:
#         break
#     print(i)

# print("hello jii")                               

# using loop inside of else
# for i in range(0,10):
#     if i==4+1:
#         # continue
#         break
#     print(i)
# else:
#     print("hello jii")
# i=1
# while i<10:
#     print(i) #the line of run infinity loop
#     i = i+1 #manualy increace a counting
    
# else:
#     print("hello paul")

# for letter in 'geeksforgeeks':
 
#     # break the loop as soon it sees 'e'
#     # or 's'
#     if letter == 'e' or letter == 's':
#         break
 
# print('Current Letter :', letter)


# An empty loop
for letter in 'geeksforgeeks':
	if letter=="e":
		pass
	
	
print('Last Letter :', letter)









