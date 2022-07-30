#find the larget number in the given list
no_of_input=int(input('enter the number of input\n'))
my_list=[]
new_list=[]

while no_of_input>0:
    my_list.append(int(input('enter the value\n')))
    no_of_input=no_of_input - 1

my_list.sort()
new_list=my_list[:]
print('the larget nubmber is --> ',new_list[no_of_input-1])
