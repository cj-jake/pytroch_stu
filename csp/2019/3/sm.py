# n=int(input())
# nums=list(map(int,input().split()))
# mid = (nums[(n - 1) // 2] + nums[n // 2]) / 2
# if int(mid) == mid:
#     mid = int(mid)
#
#
# print("{} {} {}".format(max(nums), round(mid, 1), min(nums)))


n = int(input())
T = 0
D = 0
E = 0
# 记录苹果掉落得棵树
st = [0] * n
for i in range(n):
    apples = list(map(int, input().split()))
    T1 = apples[1]
    falg=False
    for apple in apples[2:]:
        if apple<= 0:
            T1 += apple
        else:
            if T1 != apple:
                T1 = apple
                falg=True
    if falg:
        D += 1
        st[i] = 1
    T += T1
    # 进行E得计算
if st[n - 1] == st[n - 2] == st[0] == 1:
    E += 1
if st[n - 1] == st[0] == st[1] == 1:
    E += 1
for i in range(n - 2):
    if st[i] == st[i + 1] == st[i + 2] == 1:
        E += 1

print(f"{T} {D} {E}")
