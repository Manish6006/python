aIntNum=0

try:
    aIntNum=int(input('enter the inetger value\n'))
    for number in [23,7,1,9,33,2,1]:
        if number<aIntNum:
            print(number,aIntNum)
except:
    print('Integer is accepted only')