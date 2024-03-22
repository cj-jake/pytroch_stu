n, m = map(int, input().split())
A = set()
B = set()
for i in range(n):
    x, y, tp = input().split()
    if tp == "A":
        A.add(tuple([x, y]))
    else:
        B.add(tuple([x, y]))
querys = []
for i in range(m):
    querys.append(list(map(int, input().split())))
"""
    A_cnt = len(A)
    B_cnt = len(B)
    统计下标下面总共多少个 
    A 如何在全部在上面 则B必然全部在下面 结果位YES 反之一样
    第一个for 判断是否在上面 如果A_cnt一直减到0 表明在上面  用falg 记录一下 B需要和他相反
    如果没有减到0 判断是否全部在下面  如果A_cnt没有减到0 则直接可以进行下一次判断
    对于B 使用falg 进行相反得判断
"""
for query in querys:
    A_cnt = len(A)
    B_cnt = len(B)
    falg = 0
    for x, y in A:
        if query[1] * int(x) + query[0]>-query[2]*int(y):
            A_cnt -= 1
    if A_cnt == 0:
        falg = 1
    else:
        A_cnt = len(A)
        for x, y in A:
            if query[1] * int(x) + query[0]<-query[2]*int(y):
                A_cnt -= 1
    if A_cnt != 0:
        print("No")
        continue
    for x, y in B:
        if falg == 0:
            if query[1] * int(x) + query[0]>-query[2]*int(y):
                B_cnt -= 1
        else:
            if query[1] * int(x) + query[0]<-query[2]*int(y):
                B_cnt -= 1
    if B_cnt == 0:
        print("Yes")
    else:
        print("No")
