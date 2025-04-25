
def bubble_sort(arr):
    if len(arr)<=1:
        return
    for i in range(len(arr)-1):
        flag=True
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                flag=False
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if flag:
            return



arr = [20, 15, 25, 10, 30, 35, 60, 55, 40, 65, 80, 70]
bubble_sort(arr)
print(arr)
