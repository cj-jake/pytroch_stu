n,a,b=map(int,input().split(' '))
areas=[]
for i in range(n):
    areas.append(list(map(lambda x: max(0, int(x)), input().split(' '))))

ans=0
for area in  areas:
    wight=0
    hight=0
    if area[0]>=a or area[1]>=b:
        continue
    if area[2]>a:
        wight=a-area[0]
    else:
        wight=area[2]-area[0]
    if area[3]>b:
        hight=b-area[1]
    else:
        hight=area[3]-area[1]
    ans+=wight*hight
print(ans)

