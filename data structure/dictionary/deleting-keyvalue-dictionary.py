'''''
This is an example for DELETING THE KEY VALUE PAIR FROM DICTIONARY
'''''
#create the dictionary
newDictionary={
    'firstname':'hello',
    'middlename':'happy',
    'lastname':'world',
    'age':35,
    'emailid':'helloworld@example.com',
    'address':'computer memory'
}

#Before deleting the key value pair
print('Before deleting the key value pair \n', newDictionary)

#deleting the key value pair
del newDictionary['address']

#After deleting the key value pair
print('After deleting the key value pair \n', newDictionary)
