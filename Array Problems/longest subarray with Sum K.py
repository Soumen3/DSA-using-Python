def lenOfSubArray(arr, target):
    subarrays=[]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            subarray=arr[i:j]
            if sum(subarray)==target:
                subarrays.append(subarray)
    max_len=len(subarrays[0])
    for i in range(1,len(subarrays)):
        if len(subarrays[i])>max_len:
            max_len=len(subarrays[i])
    return max_len

arr=[int(e) for e in input("Enter the array elements seperated by space: ").split(' ')]
target=int (input("Enter the target element: "))
length=lenOfSubArray(arr, target)
print("The length of the longest sub array is: ",length)




# def get_all_suarrays(arr):
#     subarrays=[]
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)+1):
#             subarray=arr[i:j]
#             subarrays.append(subarray)
#     return subarrays

