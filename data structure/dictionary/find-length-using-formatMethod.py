'''
This is an example for FINDING THE LENGTH OF THE DICTIONARY USING FORMAT METHOD
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

# Method 1
print('\n There are {} key-value pairs available in dictionary'.format(len(newDictionary)),'\n')
# Method 2
print('firstname: {} ,\nemailid: {} ,\naddress: {} '.format(newDictionary['firstname'],newDictionary['emailid'],newDictionary['address']))
