#method 1
int_var=764.37
print(str(int_var))
print(type(int_var))

#method 2
int_var=1.212
print("% s" % int_var)
print(type(int_var))

#method 3
int_var=9873.7
print("{}".format(int_var))
print(type(int_var))

#method 4
int_var=45.32
print(f'{int_var}')
print(type(int_var))

#method 5
int_var=2124.90
print(int_var.__str__())
print(type(int_var))