import math

n,X,Y=map(int,input().split())
sites=[]
for i in range(n):
    sites.append(list(map(int,input().split())))
sites_sort={}
for i,site in enumerate(sites):
    distance=math.pow(X-site[0],2)+math.pow(Y-site[1],2)
    if distance  in sites_sort.keys():
        sites_sort[distance].append(i+1)
    else:
        sites_sort[distance]=[i + 1]
sites_sort=sorted(sites_sort.items(),key=lambda x:x[0])
i=0
for key,value in sites_sort:
    for v in value:
        print(v)
        i+=1
        if i==3:
            break
    if i == 3:
        break