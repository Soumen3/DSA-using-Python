def findLarge(arr):
    large=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>large:
            large=arr[i]
    return large

arr= [eval(e) for e in input("Enter the array elements seperated by space: ").split(' ')]
largest=findLarge(arr)
print("The largest element is ",largest)

# python function 
print("The largest number is : ",max(arr))