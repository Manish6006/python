#take integer input
aInt=0
try:
    aInt=int(input('enter int value \n'))
    print("the input value is ",aInt," entered\n")
except:
    print("the inital value is ",aInt)

#take float input
aFloat=0.0
try:
    aFloat=float(input('enter float value \n'))
    print("the input value is ",aFloat," entered\n")
except:
    print("the inital value is ",aFloat)


#take string input
aString=" "
try:
    aString=input('enter string value \n')
    print("the input value is ",aString," entered\n")
except:
    print("the inital value is ",aString)