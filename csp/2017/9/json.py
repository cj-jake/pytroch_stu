import json

n,m=map(int,input().split())
json_str=''
for i in  range(n):
    json_str+=input()

json_obj=json.loads(json_str)

