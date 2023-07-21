def add(n):
    return n+n

l = [1,2,3,4,5,6]

s=map(add,l)

print(list(s))

def fun (V):
    l  = ['a','e','i','o','u']
    if V in l:
        return True
    else:
        return False
    
h = ['a','q','o','u','r','i','t']
f = filter(fun,h)

print(list(f))

