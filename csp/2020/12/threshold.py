n=int(input())
nums=[]
for i in range(n):
    t=list(map(int, input().split()))
    nums.append(t)
#预测正确次数
nums.sort()
threshold=[]
result=[]
for x in nums:
    threshold.append(x[0])
    result.append(x[1])
max_ans=0
max_cnt=0
for thred in threshold:
    ans=0
    for i in range(n):
        if threshold[i] >= thred:
            predict=1
        else:
            predict=0
        if  predict==result[i]:
            ans+=1
    if ans>=max_cnt:
        max_ans=thred
        max_cnt=ans
print(max_ans)


