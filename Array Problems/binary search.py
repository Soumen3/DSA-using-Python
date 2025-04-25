def search(arr, ele):
    arr.sort()
    return arr.index(ele)


arr=[eval(e)  for e in input("Enter the element separated by space: ").split(' ')]
index=search(arr,ele=eval(input("Enter the element: ")))
print("After sorting the array: ", arr)
print("the index of the element is: ",index)
