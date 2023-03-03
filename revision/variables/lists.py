#This is an example for lists variable 

#creating the list
list=[1,6,4,8,2,9,6,5]

print(list)

## indexing returns the item
list=[1,6,4,8,2,9,6,5]
print(list[0])
print(list[-1])
print(list[-1:])
print(list[:-1])
print(list[-3:])
print(list[:])

#Lists also su
# pport operations like concatenation:
list=[1,6,4,8,2,9,6,5]
print(list + [3,0,5,9,2,1,0])

#Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
list=[1,6,4,8,2,9,6,5]
list[1]=0
print(list)

#You can also add new items at the end of the list, by using the append() method
list=[1,6,4,8,2,9,6,5]
list.append(4425)
print(list)

#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
list=['a','s','s','i','g','n','m','e','n','t']
print(list)
print(list[:])
print(list[3:6])
list[-1]='T'

print(list)

## replace some values
list=['a','s','s','i','g','n','m','e','n','t']
print(list)
list[1:3]=['S','S']
print(list)

# now remove them
list=['a','s','s','i','g','n','m','e','n','t']
print(list)
list[1:4]=[]
print(list)

#remove all the characters
list=['a','s','s','i','g','n','m','e','n','t']
print(list)
print(list[:])
list[:]=[]
print(list)

#find the list 
list=['a','s','s','i','g','n','m','e','n','t']
print(list)
print(len(list))

#It is possible to nest lists (create lists containing other lists), for example:
list=['a','s','s','i','g','n','m','e','n','t']
print(list)
list1=[1,2,4,6,9,0]
print(list1)
resList=[list,list1]
print(resList)