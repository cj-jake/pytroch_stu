n = int(input())
grap = []
grap_set = set()
for i in range(n):
    t = list(map(int, input().split()))
    grap.append(t)
    grap_set.add(tuple(t))

# 进行寻址 适合选址得记录下来并计算得分
socres = [0, 0, 0, 0, 0]
# 各个方向的
dricetions = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
for site in grap:
    is_address = 0
    socre = 0
    for x, y in dricetions[0:4]:
        new_site = tuple([x + site[0], y + site[1]])
        if new_site in grap_set:
            is_address += 1
        else:
            break
    #is_address==t4 表明可以是垃圾站
    if is_address == 4:
        for x, y in dricetions[4:]:
            new_site = tuple([x + site[0], y + site[1]])
            if new_site in grap_set:
                socre+=1
        socres[socre] += 1
for socre in socres:
    print(socre)
