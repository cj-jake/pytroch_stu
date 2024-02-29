# 命令行选项
options = list(input())
has_option = []
no_option = []
for option in options:
    if option == ':':
        last = no_option.pop()
        has_option.append(last)
    else:
        no_option.append('-' + option)
print(has_option)
print(no_option)
n = int(input())
ans = []
for i in range(n):
    command = list(input().split(' '))
    temp = []
    if len(command) == 1:
        ans.append(temp)
        continue
    if len(command)==0:
        break
    falg = -1
    falgSTr = ''
    for j in range(1, len(command)):
        opt = command[j]
        if opt.isdigit(): continue
        if opt in no_option:
            if opt not in temp:
                temp.append(opt)
        elif opt in has_option:
            if (opt + ' ' + falgSTr) in temp:
                temp[falg] = opt + ' ' + command[j + 1]
            else:
                falgSTr = command[j + 1]
                temp.append(opt + ' ' + command[j + 1])
                falg = j - 1
        else:
            break
    ans.append(temp)

ans_sort = [sorted(sublist) for sublist in ans]
for i, ans in enumerate(ans_sort):
    print(f'Case {i + 1}: {" ".join(t for t in ans)}')
