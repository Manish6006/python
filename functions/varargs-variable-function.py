'''
this is program for "VarArgs parameters" using the function.
'''
def varargs_function(a=5, *phone, **dicitonary):
    print('Value of a is ', a ,'\n')

    for phone_items in phone:
        print('printing phone_items is ',phone_items,'\n')
    
    for dicitonary_items_1,dicitonary_items_2 in dicitonary.items():
        print(dicitonary_items_1,'\t',dicitonary_items_2)

varargs_function(10,3,6,7,8,9,2,manish=6006,kumar=1206,sharma=96666)

