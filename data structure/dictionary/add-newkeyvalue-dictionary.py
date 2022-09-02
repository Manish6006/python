'''''
This is an example for ADDING NEW KEY VALUE PAIR IN THE DICTIONARY
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

#displaying the key value pairs before adding the new key value pair
print('before adding the new key value pair \n', newDictionary)

#adding new key value pair
newDictionary['zipcode']=12345

#displaying the key value pairs after adding the new key value pair
print('after adding the new key value pair \n', newDictionary)