def sum(nums, target):
    nums.sort()
    result=[]
    
    for i in range(len(nums)-1):
        for j in range (i+1 , len(nums)):
            l=len(nums)-1
            k=j+1
            while(k<l):
                if (target - (nums[i]+nums[j])) > (nums[k]+nums[l]):
                    k+=1
                elif (target - (nums[i]+nums[j])) < (nums[k]+nums[l]):
                    l-=1
                else:
                    if [nums[i],nums[j],nums[k],nums[l]] not in result:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                    else:
                        k+=1
                        l-=1
    
    return result



nums = [1,0,-1,0,-2,2]
target = 0
print("results are: ",sum(nums,target))