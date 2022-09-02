'''''
This is an example for DISPLAYING THE CONTENT BASED ON KEY 
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

#print Dictionary
print(newDictionary)

#Print key value
print('The Key is emailid and value is ', newDictionary['emailid'] )

#Print another Key value 
print('The Keys are firstname, middlename, lastname and values are ',
 newDictionary['firstname'],',',
  newDictionary['middlename'], ',',
   newDictionary['lastname'])
