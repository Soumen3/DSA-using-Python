def merge(left, right):
    i,j=0,0
    sorted_elements=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_elements.append(left[i])
            i+=1
        else:
            sorted_elements.append(right[j])
            j+=1
    sorted_elements.extend(left[i:])
    sorted_elements.extend(right[j:])
    return sorted_elements 


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    left_list=merge_sort(arr[:len(arr)//2])
    right_list=merge_sort(arr[len(arr)//2:])
    sorted_list=merge(left_list, right_list)
    return sorted_list


arr = [20, 15, 25, 10, 30, 35, 60, 55, 40, 65, 80, 70]
print(merge_sort(arr))
