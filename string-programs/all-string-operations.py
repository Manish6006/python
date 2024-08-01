temp="hello, world"
print ("capital function",temp.capitalize())
print ("title function",temp.title())
print ("uppar function",temp.upper())

myList=[1,7,2,8,9,3,5,6,7,0,3,1,6,8,9,55]
print("myList",myList)

mySet={1,5,7,1,8,9,0,5,3,2,57,3.6}
print("mySet",mySet)

myTuple=(1,4,2,5,7,9,2,3,3,2.36)
print("myTuple",myTuple)
print("====================================\n")
print("from list to Set", set(myList))
print("from list to tuple",tuple(myList))
print("From set to list", list(mySet))
print("from set to tuple",tuple(mySet))

myStr="manishKumar45263Sharma"
if myStr.isdigit():
    print("yes")
else :
    print("no")

anotherStr="hello, world, hello, world !!!!, python!"
print("count of repeated word", anotherStr.count("world"))

print("checking start with and end with", anotherStr.startswith("hello"), anotherStr.endswith("python"))

string="he said, \"hello, world\""
print("print with backslash", string)

string=r"c:\users\document\hello.txt"
print("raw string", string)

print("my string format {} and more Sstring {}".format(anotherStr,string))
#print("my string format {} and more Sstring {}"% (anotherStr,string))
print(f"my string format {anotherStr} and more Sstring {string}")

print("my string is alpha-numeric-->", myStr.isalnum())
print("my string is alphabetic-->", myStr.isalpha())
print("my string is numeric-->", myStr.isdigit())

string="           manish,      kumar,     sharma  ! ! ! ! 1 ! !   "
print("Remove space from left--->", string.lstrip())
print("Remove space from right--->", string.rstrip())
print("Remove space from all--->", string.strip())
print("Remove space from all--->", string.replace(" ",""))

stringList=["manish","kumar","sharma","python"]
print("Joinging 2 strings--->"," ".join(stringList))

print("spiliting string based on space character--->", anotherStr.split(","))

print("all uppar case-->", anotherStr.upper())
print("all lower case-->", anotherStr.lower())
print("all only first starting character-->", anotherStr.title())
print("only first character of first string-->", anotherStr.capitalize())

print("replace the string from world to manish--->", anotherStr.replace("world","Manish"))

print("find the characters--->", anotherStr.find("pythoN"))

print("slaicing the string-->", anotherStr[0:5])

print("repeating the string-->", anotherStr*4)

print("jonining 2 strings--->", anotherStr + string)
