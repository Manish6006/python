'''
This is an example for CREATING THE LOACL, NON LOCAL, AND GLOBAL VARIABLE
'''
def head_function():
    def local_func():
        hello="this is calling from local_func"

    def non_local_func():
        nonlocal hello
        hello="this is calling from non_local_func"

    def global_func():
        global hello
        hello="This is calling from global_func"
    
    hello="this is calling from head function"
    local_func()
    print("After local assignment: ", hello)
    non_local_func()
    print("After non local assignment: ", hello)
    global_func()
    print('global assignment: ', hello)

head_function()
print('In the global scope:', hello)
