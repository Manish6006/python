'''
This is an example for VALIDATING AN ITEM BELONGS TO SET data structure or not
'''

#set
superHeroSet=set(['ironman','spiderman','superman','batman','wonder women','caption america'])
print('Set:', superHeroSet)


if 'ironman' in superHeroSet:
    print('\nYes, The item is exist')
else:
    print('Item is not found')