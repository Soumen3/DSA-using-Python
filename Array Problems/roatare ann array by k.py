def rotate(arr,k):
    for i in range(k):
        lastElement=arr.pop()
        arr.insert(0,lastElement)

arr=[int(e) for e in input('Enter the array elements separated by space: ').split(' ')]
k =int(input("Enter the value of k: "))
rotate(arr,k)
print("The array after rotate:")
print(arr)