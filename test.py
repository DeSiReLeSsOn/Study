def no_repeat(s, target):
    start = 0 
    end = 0 
    maxLen = 0
    res = set() 
    while end < len(s):
        if  s[end] not in res:
            res.add(s[end]) 
            end += 1
            maxLen = max(maxLen, end - start)
        else:
            res.remove([s[start]]) 
            start += 1
    return maxLen

    
