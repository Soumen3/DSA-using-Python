
def missing(nums):
    nums.sort()
    check=1
    for i in range(len(nums)):
        if nums[i]>0:
            if nums[i]!=check:
                if nums[i]!=check-1:
                    return check
            else:
                check+=1
    else:
        if nums[-1]>0:
            return nums[-1]+1
        else: return 1

nums = [-5]
# nums =[0,2,2,1,1]
# nums =[1,2,0]

missing_num=missing(nums)
print("Missing number is ",missing_num)