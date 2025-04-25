import array

arr= array.array('i', [3,5,2,8,9,4,1])
print ('The array is:')
for i in arr:
    print(i, end=' ')

arr=sorted(arr)
print("\nafter sorted the array: ",arr)