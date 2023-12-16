res = []
flag = True
s = '{]'
for i in s:
    if i in '([{':
        res.append(i)
    elif i in ')]}':
        if not res:
            flag = False 
            break 
        b = res.pop()
        if b == '(' and i == ')':
            continue
        if b == '[' and i == ']':
            continue
        if b == '{' and i == '}':
            continue 
        flag = False
        break 

if flag and len(res) == 0:
    print('y')
else:
    print('n')