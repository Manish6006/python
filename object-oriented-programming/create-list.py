'''
This is an example for Creating the list using the Class 
'''

class listCreation():

    def __init__(self):
        self.newlist=[]

    def do_list(self, lastname):
        self.newlist.append(lastname)

firstObject=listCreation()
firstObject.do_list('johnson')
firstObject.do_list('Nicky')

secondObject=listCreation()
secondObject.do_list('jacob')
secondObject.do_list('chris')

print(firstObject.newlist)
print(secondObject.newlist)
        