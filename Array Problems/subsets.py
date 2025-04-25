
# Iterative Approach
def subsets(nums):
    result=[]
    for i in range(len(nums)):
        if i==0:
            result.append([])
            result.append([nums[0]])
        else:
            suArrays=len(result)
            for j in range(suArrays):
                copy=result[j].copy()
                copy.append(nums[i])
                result.append(copy)

    return result 
    
nums = [1,2,3]
sub_set=subsets(nums)
print("The subsets are: ",sub_set)