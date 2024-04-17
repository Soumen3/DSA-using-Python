
def move_zero(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            del(arr[i])
            arr.append(0)

arr=[eval(e)  for e in input("Enter the element separated by space: ").split(' ')]
move_zero(arr)
print("After moving the zeros", arr)