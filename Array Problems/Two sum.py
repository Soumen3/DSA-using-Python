def twoSum(arr, target):
    indices=[]
    for i in range(len(arr)):
        if arr[i]<target:
            lessThenTarget= arr[i]
            required=target-lessThenTarget
            if required in arr:
                indices.append(arr.index(required))
                indices.append(arr.index(lessThenTarget))
                return indices
    else:
        return "can't possible"


arr=[int(e) for e in input('Enter the array elements separated by space: ').split(' ')]
target =int(input("Enter the target: "))
result=twoSum(arr,target)
print("The result is: ",result)