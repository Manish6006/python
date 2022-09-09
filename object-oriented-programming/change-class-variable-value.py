'''
This is an example for CHANGE CLASS VARIABLE VALUE
'''

class myclass:
    country='Oregon'
    population='2.6 lakhs'

firstObject=myclass()
print('Country is :',firstObject.country)
print('Population is :',firstObject.population)

secondObject=myclass()
secondObject.country='Washington DC'
secondObject.population='75.1 lakhs'
print('Country is :',secondObject.country)
print('Population is :',secondObject.population)

