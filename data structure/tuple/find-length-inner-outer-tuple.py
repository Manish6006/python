'''
This is an example for FINOUT TOTAL LENGTH FOR INNER AND OUTER TUPLE
'''
innerTuple=('first','second','third','fourth',5,6,7,8,9)
outerTuple=('two','one','three',innerTuple)

#INNER TUPLE LENGTH
print('Inner Tuple Length: ', len(innerTuple))

#OUTER TUPLE LENGTH
print('Outer Tuple Length: ', len(outerTuple))

#Total length with inner & outer tuple length
print('Total length with inner and outer tuple is :', (len(outerTuple)-1)+len(outerTuple[3]))