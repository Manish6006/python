total=0
counting=0
for number in [99,100,101,87,1,4,2,6,9]:
    print('total = total + number')
    print(total,' = ',total,' + ',number)
    total=total+number
    counting=counting + 1
print('final total = ',total,'\n')
print('Average of all the above numbers= ',total/counting)