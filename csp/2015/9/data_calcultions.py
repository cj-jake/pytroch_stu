"""
使用一个数组活着map 记录每一个都多烧钱  （可以使用前缀数组计算出 这个月的之前的天数和）
如果是闰年2月份需要加上一天
总天天数依次减去月份的天数 知道不够钱剩下的就是日期
"""
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

#判断是否是闰年
def is_leap_year(year:int)->bool:
    return (year%4==0 and year%100!=0) or year%400==0
#读入数据
year=int(input())
d=int(input())
if is_leap_year(year):months[2]=29
else:months[2]=28
ans_month=1
while d>months[ans_month]:
    d-=months[ans_month]
    ans_month+=1
print(ans_month)
print(d)