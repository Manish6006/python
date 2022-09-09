'''
Class variables are shared - they can be accessed by all instances of that class.
There is only one copy of the class variable and when any one object makes a change to a class variable,
that change will be seen by all the other instances.
'''
class variable_class:
    country='India'
    print('shared by all the objects are created, it will print only one single time: \n',country)


firstObject=variable_class() #first object created
firstObject.country

secondObject=variable_class() #second object created
secondObject.country



