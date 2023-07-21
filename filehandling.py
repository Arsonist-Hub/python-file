a = open("file.exe",'w')
a.write("hello world")
a.close()

b = open("file.exe",'r')
r=b.read()
print(r)
b.close()


c= open("file.exe",'a')
c.write("python programing")
c.close()

d= open("file.exe",'r+')
d.write("overide")
print(d.read)
d.close()

