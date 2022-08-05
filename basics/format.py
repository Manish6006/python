'''
this is program for format() function
'''
try:
    age=int(input("enter the age\n"))
    name=input("enter the first name\n")
    ''' first method'''
    print('{0} is my first name and my {1} is my age'.format(name,age))
    ''' second method'''
    print('{} is my first name and my {} is my age'.format(name,age))
    ''' third method'''
    print('{name} is my first name and my {age} is my age'.format(name=name,age=age))
    ''' fourth method'''
    print(f'{name} is my first name and my {age} is my age')
except:
    print("Terminated abnormally\n")

print("finished")