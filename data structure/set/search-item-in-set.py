'''
This is an example for SEARCH AN INPUT ITEM IN SET data structure
'''

#set
superHeroSet=set(['ironman','spiderman','superman','batman','wonderwomen','captionamerica'])
print('Set:', superHeroSet)


search_item=None

def search_an_item(search_item):
        for item in superHeroSet:
            if search_item==item:
                print('Item found: ', search_item)
                break
            else:
                print('not found')
try:
        search_item=input('enter an item name which need to be searched: ')
        search_an_item(search_item)     
except:
        print('Something is not correct')
finally:
        print('search is completed')




   
            


