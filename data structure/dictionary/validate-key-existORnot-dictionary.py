'''
This is an example for  
'''
#Dictionary
newDictionary={
    'firstname':'hello',
    'middlename':'happy',
    'lastname':'world',
    'age':35,
    'emailid':'helloworld@example.com',
    'address':'computer memory'
}

#print
print(newDictionary)


if 'firstname' in newDictionary:
    print('The key is exist and\nvalue is ', newDictionary['firstname'])
else:
    print('The key is not exist')
