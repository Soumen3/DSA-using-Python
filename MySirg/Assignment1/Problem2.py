arr=[3,5,2,'t','s',4,1,'r', 4.9]

print ('The array is:')
for i in arr:
    print(i, end=' ')

i=0
while i<len(arr):
    if not isinstance(arr[i],int):
        arr.remove(arr[i])
        i-=1
    i+=1


print ('After removing non integer element The array is:')
for i in arr:
    print(i, end=' ')