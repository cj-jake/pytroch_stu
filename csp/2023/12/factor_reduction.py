# p=int(input())
# n,k=map(int,input().split())
#
# def is_su(i):
#     if i<=3: return True
#     for j in range(2,pow(i,0.5)):
#         if i//j==0:
#             return False
#     return True
#
# for i in range(2,n):
#     if is_su(i):
#         cnt=0
#         while cnt<k:
#             t=n//i
#             cnt+=1
#             if type(t) is not int:
#                 break
#             else:
#                 n//=i
#         if cnt>=k:
#             continue
#         else:
#             n*=pow(i,cnt)
# print(n)

# max_val = 100000
# primes = []
# for i in range(2, max_val):
#     if all(i % p != 0 for p in primes if p * p <= i):
#         primes.append(i)
#
# q = int(input())
# for _ in range(q):
#     n, k = map(int, input().split())
#     ans = n
#     cnt = [0] * max_val
#     for prime in primes:
#         while n % prime == 0:
#             n //= prime
#             cnt[prime] += 1
#
#     ans //= n
#     for prime, t in enumerate(cnt):
#         if t < k and t != 0:
#             ans //= pow(prime, t)
#
#     print(ans)

#计算出所有的素数
max_val = 100000
primes = []
for i in range(2, max_val):
    if all(i%prime!=0 for prime in  primes if prime*prime<=i):
        primes.append(i)


q=int(input())
nums=list()
for i in range(q):
    nums.append(map(int,input().split()))

for n,k in nums:
    cnt=[0]*max_val
    temp=n
    for prime in primes:
        while n%prime==0:
            n//=prime
            cnt[prime]+=1
    ans=1
    for prime,cnt_s in enumerate(cnt):
        if cnt_s>=k:
            ans*=pow(prime,cnt_s)
    print(ans)

