n,m=map(int,input().split())
dx=0
dy=0
for i in range(n):
    t=list(map(int,input().split()))
    dx+=t[0]
    dy+=t[1]

for i in range(m):
    t = list(map(int, input().split()))
    print(f'{t[0]+dx} {t[1]+dy}')
