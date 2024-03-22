n=int(input())
count=0
list_count=[0,0,0,0]
while n>0:
    count+=1
    if count%7==0 or '7' in str(count):
        list_count[count%4-1]+=1
    else:
        n-=1
for item in list_count:
    print(item)


