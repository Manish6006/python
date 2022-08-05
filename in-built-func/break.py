#break the loop using break keyword

aStr=''
value=0
while True:
    aStr=input('enter the special character\n')
    if aStr=='?':
        print('match found after ',value,'attempt')
        break
    else:
        print('attempt -->',value + 1,'\n')
print('loop is completed\n') 
