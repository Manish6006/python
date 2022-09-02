'''''
This is an example for DISPLAYING THE KEY VALUE USING FOR LOOP
'''''

#Dictionary
newDictionary={
    'firstname':'hello',
    'middlename':'happy',
    'lastname':'world',
    'age':35,
    'emailid':'helloworld@example.com',
    'address':'computer memory'
}
for key, value in newDictionary.items():
    print('key: {},\tvalue: {} '.format(key,value))
