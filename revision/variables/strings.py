# this is an example for Strings variables

# single quotes
str='single quotes'
print(str)

#double quotes
str="double quotes"
print(str)

#adding single quotes
str='doesn\'t'
print(str)

#adding double quotes
str="doesn\'t"
print(str)

#Display '"Yes," they said.'
str='"Yes, " they said.'
print(str)

#Display "\"Yes,\" they said."
str="\"Yes, \" they said."
print(str)

#If you don’t want characters prefaced by \ to be interpreted 
# as special characters, you can use raw strings by adding an r before the first quote:
#print('C:\Users\vdshdhjtrjtrjtjtrjtrj')
print(r'C:\Users\egrhehtrjrkkyk')

#String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. 
# End of lines are automatically included in the string, 
# but it’s possible to prevent this by adding a \ at the end of the line. 
# The following example:

str="""
hello, this is first line
and this is second line
this is third line 
this is fourth line
"""
print(str)

str='''
hello, this is first line
and this is second line
this is third line 
this is fourth line using single quotes
'''
print(str)

####Strings can be concatenated (glued together) with the + operator, and repeated with *:
str='hello'
str=str*3
str=str+'world'
print(str)

#Two or more string literals (i.e. the ones enclosed between quotes) 
# next to each other are automatically concatenated.
str=('avenger' 'assemble')
print(str)

#If you want to concatenate variables or a variable and a literal, use +:
str='new'
str=str + 'world'
print(str)

#Strings can be indexed (subscripted), with the first character having index 0.
#  There is no separate character type; a character is simply a string of size one:

str='this is new world'
print(str[0])
print(str[5])

#Indices may also be negative numbers, to start counting from the right:
str='this is new world'
print(str[-1])
print(str[-7])

#In addition to indexing, slicing is also supported. 
# While indexing is used to obtain individual characters, 
# slicing allows you to obtain substring:
str='this is new world'
print(str[0:4])

#Slice indices have useful defaults; an omitted first index defaults to zero,
#  an omitted second index defaults to the size of the string being sliced.
str='this is new world'
print(str[:2]) # character from the beginning to position 2 (excluded)
print(str[4:])
print(str[:-2])
print(str[-2:])

#The built-in function len() returns the length of a string:
str='this is new world'
print(len(str))