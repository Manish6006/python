'''''
This is an example for SLICING OPERATION IN THE SEQUENCE
'''''
countryName=['India','America','Singapore','Hong Kong','Chile','Peru']
nameString='Joseph'

def slicing_operation_countryName():
    print('Print items from 1 to 3 :', countryName[1:3]) # last index value will always be EXCLUSIVE
    print('Print items from 2 to till end :', countryName[2:])
    print('Print items from beginning to second last :', countryName[0:-1])
    print('Print items from beginning to till end :', countryName[:])
slicing_operation_countryName()

def slicing_operation_nameString():
    print('\n-------------------------------------------------------------')
    print('Print Characters from 0 to till 3 :', nameString[0:4])
    print('Print characters from beginning to till end :', nameString[:])
    print('Print Characters from 1 to till -1 :', nameString[1:-1])
slicing_operation_nameString()
