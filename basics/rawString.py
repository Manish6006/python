'''
this is an example for the raw string
'''
try:
    aStr="Newlines are indicated by \n"
    bStr='Newlines are indicated by \n'
    cStr=r'Newlines are indicated by \n'
    dStr=r"Newlines are indicated by \n"
    print(aStr,bStr,cStr,dStr)
except:
    print('Ended Abnromally')

print('finished')
