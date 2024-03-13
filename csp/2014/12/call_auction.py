# # 定义函数计算开盘价下的成交量
# def calculate_buy(open_price, orders):
#     volume = 0
#     for order in orders:
#         price, quantity = order
#         if price >= open_price:
#             volume += quantity
#     return volume
# def calculate_sell(open_price, orders):
#     volume = 0
#     for order in orders:
#         price, quantity = order
#         if price <= open_price:
#             volume += quantity
#     return volume
#
# # 存储买单和卖单
# buy_orders = []
# sell_orders = []
# orders=[]
# # 处理输入记录
# while True:
#     try:
#         record = input().split()
#         if len(record)<=0:break
#         orders.append(record)
#         if record[0]=='cancel':
#             del orders[int(record[1])-1]
#     except EOFError:
#         break
#
# # 对买单和卖单按照价格进行排序
# for record in orders:
#     if record[0] == 'buy':
#         buy_orders.append((float(record[1]), int(record[2])))
#     elif record[0] == 'sell':
#         sell_orders.append((float(record[1]), int(record[2])))
#
# buy_orders.sort(reverse=True)
# sell_orders.sort()
#
# # 从最高价格开始尝试作为开盘价
# max_volume = 0
# max_open_price = 0.00
#
# for order in buy_orders + sell_orders:
#     open_price = order[0]
#     volume = min(calculate_buy(open_price, buy_orders),calculate_sell(open_price, sell_orders))
#
#     if volume > max_volume :
#         max_volume = volume
#         max_open_price = open_price
#
# # 输出结果，保留两位小数
# print(f"{max_open_price:.2f} {max_volume}")



import sys
records = []

# ctrl+D stop
for line in sys.stdin:
    record = line.split()
    records.append(record)

# search 'cancel' and set it as ""; transfer "buy" and "sell" string data as float or int type
for record in records:
    if record[0] == 'cancel':
        record[0] = ""
        records[int(record[1])-1][0]=""
    elif record[0] in ["buy","sell"]:
        # price
        record[1] = float(record[1])
        # number
        record[2] = int(record[2])

# delete "" record
new_records = []
for i in range(len(records)):
    if records[i][0]!="":
        new_records.append(records[i])


"""
如果开盘价为p0，则系统可以将所有出价至少为p0的买单和所有出价至多为p0的卖单进行匹配。
因此，此时的开盘成交量为出价至少为p0的买单的总股数和所有出价至多为p0的卖单的总股数之间的较小值。
"""
# sort from big to small by 'price' index
"""
[['buy', 100.0, 50], ['sell', 9.0, 1000],
['buy', 9.0, 400], ['sell', 8.92, 400], ['buy', 8.88, 175]]

"""
new_records.sort(key=(lambda x:x[1]),reverse=True)

buyList = {}
lastbuy = 0

for name,price,number in new_records:
    if name == "buy":
        # 买 出价越高越好：出价高于当前值的都可以成交 记录当前价格可以成交的股数
        lastbuy+=number
    buyList[price] = lastbuy
# {100.0: 50, 9.0: 450, 8.92: 450, 8.88: 625}
#print(buyList)


sellList = {}
lastsell = 0

new_records.sort(key=(lambda x:x[1])) # small to big

for name,price,number in new_records:
    if name == "sell":
        # 买家出价为p0,卖家小于p0的卖出价都可以成交
        lastsell += number
    sellList[price]=lastsell
# print(sellList)
# {8.88: 0, 8.92: 400, 9.0: 1400, 100.0: 1400}

prices = list(buyList)
max_number = 0
best_price = 0
# print(prices)
# [100.0, 9.0, 8.92, 8.88]

for price in prices:
    data = min(buyList[price],sellList[price])
    if data > max_number:
        best_price = price
        max_number = data

print("{:.2f} {}".format(best_price,max_number))

