
def permutation(arr):
    length=len(arr)-1
    ind=-1

    # find the index from where the number is decreasing
    for i in range(length-1,0, -1):
        if arr[i]<arr[i+1]:
            ind=i
            break
    # if the numbers are sorted in descending order reverse the array
    if ind==-1:
        arr.reverse()
        return
    
    # find the just maximum number of the index (ind) position number from the left side of the index
    for i in range(length,ind,-1):
        if arr[i]>arr[ind]:
            just_max=i
            break
    

    # swap the just maximum and the index number
    arr[ind],arr[i]=arr[i],arr[ind]

    # sort the right side of the index
    arr[ind+1:length+1].sort()




arr=[1,2,3,4]
permutation(arr)
print("The next permutation is: ",arr)
