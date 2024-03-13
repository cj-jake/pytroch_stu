"""
只能拿70
"""
n,m=map(int,input().split())
s=['']*n
for i in range(n):
    s[i]=input()
dic={}
keys=[]
for i in range(m):
    key=list(input().split(maxsplit=1))
    keys.append(key[0])
    dic[key[0]]=key[1][1:-1]
for i in  range(n):
    for key in keys:
        cnt=s[i].count(key)
        for x in range(cnt):
            index=s[i].find(key)
            s[i] = s[i][:index-3] + dic[key] + s[i][index+3 + len(key):]
    while "{{" in s[i] and "}}" in s[i]:
        index1=s[i].find("{{")
        index2=s[i].find("}}")
        s[i] = s[i][:index1] + s[i][index2 + 2:]
    print(s[i])

"""
11 2
<!DOCTYPE html>
<html>
<head>
<title>User {{ name }}</title>
</head>
<body>
<h1>{{ name }}</h1>
<p>Email: <a href="mailto:{{ email }}">{{ email }}</a></p>
<p>Address: {{ address }}</p>
</body>
</html>
name "David Beckham"
email "david@beckham.com"
"""