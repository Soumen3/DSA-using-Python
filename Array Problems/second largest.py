def findLarge(arr):
    large, sec_large=arr[0], arr[1]
    for i in range(0,len(arr)):
        if large<arr[i]:
            large=arr[i]
        elif sec_large<arr[i]:
            sec_large=arr[i]
            
    return sec_large
arr= [eval(e) for e in input("Enter the array elements seperated by space: ").split(' ')]
# arr=[eval(e) for e in input("Enter the number separated by space: ").split(' ')]
secLagre=findLarge(arr)
print("The second largest number is: ",secLagre)

# python function 
copy_array=sorted(arr,reverse=True)
print(copy_array)
print("The second largest array is: ",copy_array[1])