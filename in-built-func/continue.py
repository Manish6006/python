#break the loop using break keyword

aStr=''
value=0
while True:
    try:
        aStr=input('enter the special character\n')
        if aStr=='?':
            print('match found after ',value,'attempt')
            continue
        elif aStr=='@':
            break
        else:
            print('attempt -->',value + 1,'\n')
    except:
        print('not entered correct value')

print('loop is completed\n') 
