def m(nums, target):
    low = 0 
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2 
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

    

    




    
    


   
    


        

    

   
   
  
      
    
   
    
  

   
  


   
    
    
    
            


a = [2,7,11,15, -1]
b = 15
print(m(a, b))



