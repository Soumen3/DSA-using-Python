def insertion_sort(arr):
    if len(arr)<=1:
        return
    
    for i in range(1, len(arr)):
        key= arr[i]

        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key



arr = [20, 15, 25, 10, 30, 35, 60, 55, 40, 65, 80, 70]
insertion_sort(arr)
print(arr)
