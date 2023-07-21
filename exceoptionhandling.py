
try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a/b

except ZeroDivisionError:
    print("cannot be divided by zero")

except ValueError:
    print("input should be integer")

except:
    print("error in the program")

else :
    print(c)


# finally:
#     print("program excuted")


