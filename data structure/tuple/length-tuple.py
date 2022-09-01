'''
This is an example for find the length tuple
'''

#creating the tuple
newTuple=('firstname','middlename','lastname','surname','fullname','nickname',18,4,3)

#displaying the length of the tuple
print('The length of tuple is : ', len(newTuple))

#using FOR loop to print tuple items
i=1
for item in newTuple:
    print('the item number', i, 'is :', item)
    i+=1
