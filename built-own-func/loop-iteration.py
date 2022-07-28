# this is function used for loop iteration 
aIntNum=0
try :
    aIntNum=int(input('\n enter the value \n'))
    if aIntNum!=0:
        while aIntNum > 0:
            print('value--> ',aIntNum)
            aIntNum=aIntNum - 2
        print('while loop completed\n')
    else:
        print('enter the value greater than 0\n')
except:
    print('Integer value is only accepted\n') 
print('<-------finished----->\n')

