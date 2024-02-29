# from collections import defaultdict
#
# n,m,k=map(int,input().split(' '))
# ares=[]
# for i in range(n):
#     ares.append(list(map(int,input().split(' '))))
# ans=0
# sorted_ares = sorted(ares, key=lambda x: (-x[0],x[1]))
# ares_dict=defaultdict(int)
# for row in ares:
#     ares_dict[row[0]]+=row[1]
# sorted_dict_items = sorted(ares_dict.items(), key=lambda x: (-x[0], x[1]))
#
# # 将排序后的结果转换回字典
# sorted_dict = dict(sorted_dict_items)
#
# while m>0 and sorted_ares[0][0]>k:
#     if m>sorted_ares[0][1]:
#         m -= sorted_ares[0][1]
#         sorted_ares[0][0] -= 1
#         sorted_ares.sort(key=lambda x: (-x[0], x[1]))
#     if m<len(sorted_ares):
#         break
# ans=max(row[0] for row in sorted_ares)
#
# print(ans)
from itertools import tee

n, m, k = map(int, input().split())
ans = -1
land = {}  # 使用字典来模拟C++中的map

for _ in range(n):
    t, c = map(int, input().split())
    land[t] = land.get(t, 0) + c

land[k] = land.get(k, 0)  # 最少天数，保证每次能有两个合并

while m >= land[list(land.keys())[0]] and list(land.keys())[0] > k:
   if land:
       continue





it = iter(land)
if ans == -1:
    print(next(it))
