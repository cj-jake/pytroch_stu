n,k,t,xl,yd,xr,yu=map(int,input().split())
sites=[]
for i in range(n):
    sites.append(list(map(int,input().split())))

passed=0
state=0
for site in sites:
    tim=0
    #标记是否逗留过 和经过过
    falg_s=False
    falg=False
    for i in range(0,t*2,2):
        if xl<=site[i]<=xr and yd<=site[i+1]<=yu:
            tim+=1
            if falg_s==False:
                passed += 1
                falg_s=True
            if tim>=k and falg==False:
                state+=1
                falg=True
        else:
            tim=0
print(passed)
print(state)