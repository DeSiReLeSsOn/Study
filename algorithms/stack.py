s = input()
stack = []
flag = True
for i in s:
    if i in '([{':
        stack.append(i)
    elif i in ')]}':
        if not stack:
            flag = False
            break
        brack = stack.pop()
        if brack == '(' and i == ')':
            continue
        elif brack == '[' and i == ']':
            continue
        elif brack == '{' and i == '}':
            continue
        flag = False
        break

if flag and len(stack) == 0:
    print('yes')
else:
    print('no')