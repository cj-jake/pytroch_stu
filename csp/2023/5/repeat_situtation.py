import collections
from collections import defaultdict

n=int(input())
dicts=defaultdict(lambda: 0)
l=[]
ans=[0]*n
for i in range(n):
    s=''
    for j in range(8):
        s+=input()
    l.append(s)
    cnt = collections.Counter(l)
    ans[i]=cnt[l[i]]

for a in ans:
    print(a)