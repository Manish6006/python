# this is an example for nested  IF & ELSE 

a=True
b=False
c=True

if b==True:
    if a==False:
        print('a is false', a)
    elif c==False:
        print('c is false',c)
    else:
        print('a & c both are true: ', a,c)

print('b is false')
