'''
This is an example for APPENDING other items in the given list
'''
#defining the list 
fruitList=['apple','mango','kiwi','banana','carrot']

#displaying the list before appending the other items
print('The items are before append : ',end=' ')
for item in fruitList:
    print(item,end=' ')
print('\n')

#appending the items
fruitList.append('guawa')

#displaying the list after appending the other items
print('The items are after append : ',end=' ')
for item in fruitList:
    print(item,end=' ')
print('\n')

