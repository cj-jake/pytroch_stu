# 读入数据
# 暴力 通过80%
# import math
#
# n,m=map(int,input().split())
# opt=[]
# for i in range(n):
#     opt.append( [float(x) if '.' in x else int(x) for x in input().split()])
#
# for i in range(m):
#     i,j,x,y=map(int,input().split())
#     for k in range(i-1,j,1):
#         if opt[k][0]==1:
#             x*=opt[k][1]
#             y*=opt[k][1]
#         elif opt[k][0]==2:
#             t_x,t_y=x,y
#             x=t_x*math.cos(opt[k][1])-t_y*math.sin(opt[k][1])
#             y=t_x*math.sin(opt[k][1])+t_y*math.cos(opt[k][1])
#     print(x,y)
import math

n, m = map(int, input().split())
k_ = [1.0]
e_ = [0]
for i in range(n):
    t = [float(x) if '.' in x else int(x) for x in input().split()]
    if t[0] == 1:
        k_.append(k_[i] * t[1])
        e_.append(e_[i])
    elif t[0] == 2:
        k_.append(k_[i])
        e_.append(e_[i] + t[1])

for i in range(m):
    i, j, x, y = map(int, input().split())
    k = k_[j] / k_[i - 1]
    e = e_[j] - e_[i - 1]
    x *= k
    y *= k
    t_x, t_y = x, y
    x = t_x * math.cos(e) - t_y * math.sin(e)
    y = t_x * math.sin(e) + t_y * math.cos(e)
    print(x,y)
