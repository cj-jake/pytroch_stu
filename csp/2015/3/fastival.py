"""
需要一个记录 每个月天数得数组， 同时需要判断是否是闰年
先计算出有几天到那一年 和月
"""

# 读入数据
# a, b, c, y1, y2 = map(int, input().split())
#
# months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#
# leap_year = []
# for year in range(1850, y1):
#     if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
#         leap_year.append(year)
# count_leap_year = len(leap_year)
# count_day = count_leap_year * 366 + (y1 - 1850) * 365
# temp=count_day
#
# for year in range(y1, y2 + 1):
#     temp = count_day
#     if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
#         count_day+=366
#         months[2] = 29
#     else:
#         months[2] = 28
#         count_day += 365
#     temp+=sum(months[i] for i in range(1, a))
#     #计算 天的余数  0 表示星期二  （b-1)*7
#     week=(temp+2)%7#计算出来了 a月份星期几
#     week = 7 if week == 0 else week
#     day=0
#     if c<week:
#         day+=8-week
#         week=1
#     day+=1+c-week+(b-1)*7
#     if months[a]<day:
#         print('none')
#     else:
#         print(f'{year}/{a:02d}/{day:02d}')

everyMon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 判断是否为闰年并作出相应的处理
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        everyMon[1] = 29
    else:
        everyMon[1] = 28


# 求year年month月1日是星期几
def get_week(year, month):
    total_days = (year - 1850) * 365
    for i in range(1850, year):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            total_days += 1
    leap_year(year)
    for i in range(1, month):
        total_days += everyMon[i - 1]
    week = (total_days + 2) % 7
    return 7 if week == 0 else week


# 求year年a月第b个星期c是几号
def get_day(year, a, b, c):
    week = get_week(year, a)
    leap_year(year)
    for i in range(0, everyMon[a - 1]):
        c %= 7
        if week % 7 == c:
            b -= 1
        if b == 0:
            break
        week += 1
    if b:
        print("none")
    else:
        print(f"{year}/{a:02d}/{i + 1:02d}")

a, b, c, y1, y2 = map(int, input().split())
for year in range(y1, y2 + 1):
    get_day(year, a, b, c)
