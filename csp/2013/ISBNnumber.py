char_s=input()
if char_s:
    flag=False
    sum=0
    i=1
    for index,char in enumerate(char_s[:-2]):
        if char!='-':
            sum+=int(char)*i
            i+=1
    if str(sum%11)==char_s[-1] or (sum % 11 == 10 and char_s[-1]=='X'):
        print("Right")
    else:
        char_s = char_s[:-1] + str((sum % 11) if sum % 11 != 10 else 'X')
        print(char_s)