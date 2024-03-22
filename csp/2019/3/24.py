n=int(input())

def is_true(commond):
    num_st=[]
    char_st=[-2]
    dicts={"x":5,"/":6,"+":1,"-":2}
    for i,num in enumerate(commond):
        if type(num)==int:
            num_st.append(num)
        else:
            if dicts[num]-char_st[-1]>=3:
                #入栈
                char_st.append(dicts[num])
            else:
                operations = {1: lambda a, b: a + b,
                              2: lambda a, b: a - b,
                              5: lambda a, b: a * b,
                              6: lambda a, b: a // b}
                a=num_st.pop()
                b=num_st.pop()
                operator=char_st.pop()
                c=operations.get(operator)(b,a)
                num_st.append(c)
                char_st.append(dicts[num])
    while char_st!=[-2]:
        operations = {1: lambda a, b: a + b,
                      2: lambda a, b: a - b,
                      5: lambda a, b: a * b,
                      6: lambda a, b: a // b}
        a = num_st.pop()
        b = num_st.pop()
        operator = char_st.pop()
        c = operations.get(operator)(b, a)
        num_st.append(c)
    return num_st[-1]==24



for i in  range(n):
    commond=[int(item) if item.isdigit() else item for item in list(input())]
    print("Yes" if is_true(commond) else "No")




