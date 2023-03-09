n=int(input())
lst=[]
for i in range(0,n):
    ele=int(input())
    lst.append(ele)

print(all([n in lst,n==lst]))