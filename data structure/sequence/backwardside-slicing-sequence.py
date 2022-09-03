'''
This is an example for SLICING OPERATION FROM BACKWARD SIDE FOR SEQUENCE
'''

countryName=['India','America','Singapore','Hong Kong','Chile','Peru']


def slicing_operation_countryName():
    print('Print items :', countryName[::3]) # last index value will always be EXCLUSIVE
    print('Print items :', countryName[::1])
    print('Print items :', countryName[::2])
    print('Print items :', countryName[::-1])
    print('Print items :', countryName[:])
slicing_operation_countryName()

