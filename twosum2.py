
nums =[2,7,11,15]

target =9



def twosum(nums,target):
    for i, n in enumerate(nums):
        complement =target - n

        if complement in nums[i+1:]:
        
            return nums.index(n) , nums[i+1:].index(complement)+(i+1)
            
        
                                                                
i,j =twosum(nums, target)

print(i,end='')
print(j)
