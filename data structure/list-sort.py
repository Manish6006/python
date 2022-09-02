'''
This is an example for Sorting the given list
'''
#defining the list 
vegList=['cabbage','patato','tamato','ginger','carrot']

#displaying the list before sorting List
print('The items are before sorting : ',end=' ')
for item in vegList:
    print(item,end=' ')
print('\n')

#sorting the list
vegList.sort()

#displaying the list after sorting List
print('The items are after sorting : ',end=' ')
for item in vegList:
    print(item,end=' ')
print('\n')

