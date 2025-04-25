def partition(arr, low, high):
    pivot=low

    while low<high:
        while arr[pivot] < arr[high]:
            high-=1
        arr[high], arr[pivot] = arr[pivot], arr[high]
        pivot=high

        while arr[pivot]>arr[low]:
            low+=1
        arr[low], arr[pivot]=arr[pivot], arr[low]
        pivot=low
    
    return pivot



def quick_sort(arr, low=0, high=None):
    if len(arr)<=1:
        return
    
    if high is None:
        high=len(arr)-1

    if low<high:
        PIndex=partition(arr, low, high)
        quick_sort(arr, low, PIndex-1)
        quick_sort(arr,PIndex+1, high)
    


arr = [20, 15, 25, 10, 30, 35, 60, 55, 40, 65, 80, 70]
quick_sort(arr)
print(arr)