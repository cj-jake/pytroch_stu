"""
直接服了  感觉 没有什么错误就是 不通过


"""
import re


def is_cat(expr: str):
    ans = []
    if ":" in expr:
        expr = expr.split(":")
        for item in g:
            key, value = item
            if (int(expr[0]), int(expr[1])) in value:
                ans.append(key)
        return ans
    elif "~" in expr:
        expr = expr.split("~")
        for item in g:
            key, value = item
            for tup in value:
                if tup[0] == int(expr[0]) and tup[1] != int(expr[1]):
                    ans.append(key)
            return ans
    return ans

# 读取输入
n = int(input())
g = []
for i in range(n):
    t = list(map(int, input().split()))
    # [(1, {(2, 3), (1, 2)}), (2, {(2, 3), (3, 1)})]  包装成的结果
    g.append((t[0], {(t[2 + i], t[2 + i + t[1]]) for i in range(t[1])}))

m = int(input())
expressions=[]
for i in range(m):
    expressions.append(input())
i=1
for expr in expressions:
    if expr[0] == '&':
        matches = re.findall(r'\((.*?)\)', expr)
        prev_matche = None
        for matche in matches:
            if prev_matche is not None:
                intersection = list(set(is_cat(matche)) & set(is_cat(prev_matche)))
                for a in intersection:
                    print(a, end=" ")
                if i != m: print()
            prev_matche = matche

    elif expr[0] == '|':
        matches = re.findall(r'\((.*?)\)', expr)
        for matche in matches:
            for a in is_cat(matche):
                print(a, end=" ")
        if i != m: print()

    else:
        if ":" in expr:
            expr = expr.split(":")
            for item in g:
                key, value = item
                if (int(expr[0]), int(expr[1])) in value:
                    print(key, end="")
            if i != m: print()
        elif "~" in expr:
            expr = expr.split("~")
            for item in g:
                key, value = item
                for tup in value:
                    if tup[0] == int(expr[0]) and tup[1] != int(expr[1]):
                        print(key, end="")
            if i != m: print()
    i += 1

