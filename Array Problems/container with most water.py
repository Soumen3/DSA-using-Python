def getWater(height):
    left=0
    right=len(height)-1
    ans=0
    while(left<right):
        ans=max( (min(height[left],height[right])*(right-left)),ans)
        if height[left] < height[right]:
            left+=1 
        else:
            right-=1

    return ans


height = [1,8,6,2,5,4,8,3,7]
water=getWater(height)
print("The maximum water can be store: ",water)