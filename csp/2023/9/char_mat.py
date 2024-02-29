pattern = input()
model_str = input()
n = int(input())
for i in range(n):
    text = input()
    temp=text
    if model_str == '0':
        pattern = pattern.lower()
        temp = text.lower()
    if pattern in temp:
        print(text)
