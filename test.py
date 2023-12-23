def binary_search(s):
    start = 0 
    end = 0 
    maxLen = 0 
    res = set()
    while end < len(s):
        if s[end] not in set:
            res.add(s[end])
            end += 1
            maxLen = max(maxLen, end - start) 
        else:
            res.remove(s[start])
            start += 1 
    return maxLen

   
  


   
    
    
    
            


a = [2,7,11,15]
b = 15
print(binary_search(a, b))



