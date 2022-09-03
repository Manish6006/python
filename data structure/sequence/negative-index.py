'''
This is an example for PRINT AN ITEM BASED ON NEGATIVE INDEX WISE
'''

countryName=['India','America','Singapore','Hong Kong','Chile','Peru']

# -1, -2 INDEX USED TO ACCESS THE LAST & SECOND LAST ITEM FROM SEQUENCE
print('Item[-1] : ', countryName[-1])
print('Item[-2] :', countryName[-2])

#using the len() function to print the last item
print('Item[last] :', countryName[len(countryName)-1])
print('Item[second last] :', countryName[len(countryName)-2])



