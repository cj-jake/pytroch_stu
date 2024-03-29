n,N=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.append(N)
sum=0
for i in range(1,n+1):
    sum+=i*(numbers[i]-numbers[i-1])
print(sum)