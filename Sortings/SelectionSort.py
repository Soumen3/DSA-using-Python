
def selection_sort(arr):
    for i in range(len(arr)):
        min =i
        for j in range(i+1, len(arr)):
            if arr[j]< arr[min]:
                min = j
        
        if min!=i:
            arr[min],arr[i]=arr[i],arr[min]

arr = [20, 15, 25, 10, 30, 35, 60, 55, 40, 65, 80, 70]
selection_sort(arr)
print(arr)