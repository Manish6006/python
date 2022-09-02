'''
This is an example for deleting item from the given the list
'''
#defining the list 
fruitList=['apple','mango','kiwi','banana','carrot']

#displaying the list before deleting an items
print('The items are before deleting : ',end=' ')
for item in fruitList:
    print(item,end=' ')
print('\n')

#deleting an item from the list
del fruitList[1]
#displaying the list after deleting an items
print('The items are after deleting  : ',end=' ')
for item in fruitList:
    print(item,end=' ')
print('\n')