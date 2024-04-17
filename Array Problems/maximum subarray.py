def maxSubarray(nums):
    sums=[]
    for i in range(len(nums)):
        if i ==0:
            sums.append(nums[i])
        else:
            if nums[i] < sums[-1]+nums[i]:
                sums.append(sums[-1]+nums[i])
            else:
                sums.append(nums[i])
    return max(sums)



nums = [5,4,-1,7,8]
max_subarray=maxSubarray(nums)
print("The sum maximum sub array is ",max_subarray)