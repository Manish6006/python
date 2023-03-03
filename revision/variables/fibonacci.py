#Fibonacci series

print('Enter the integer number: \n')

try:
    endNum=int(input())
    first=0
    second=1

    print(first) #0
    print(second) #1
    result=first+second #1
    for next in range(1,endNum+1):
        result=1
        next=1
        result= next+result #2



        





except:
    print('Entered number is not integer\n')

