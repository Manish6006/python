'''
This is an example for DISPLAYING THE INDEX BASED CONTENT OF THE TUPLE
'''
innerTuple=('first','second','third','fourth',5,6,7,8,9)

index=int(input('Enter the index number : \n'))
if index >=len(innerTuple):
    print('Index out of bound. Enter lower value')
else:
    print('The value is ', innerTuple[index], 'at index ', index)