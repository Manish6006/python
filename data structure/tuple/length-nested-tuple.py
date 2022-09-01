'''
This is an example for finding the LENGTH FOR NESTED TUPLE
'''
innerTuple=('first','second','third','fourth',5,6,7,8,9)
outerTuple=('two','one','three',innerTuple)

#displaying the content for INNER TUPLE
print(innerTuple)
#printing the lenght for INNER TUPLE
print('the total length is :', len(innerTuple))

#displaying the content for OUTER TUPLE
print(outerTuple)
#printing the lenght for OUTER TUPLE
print('the total length is :', len(outerTuple))