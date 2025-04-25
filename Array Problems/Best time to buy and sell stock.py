def prediction(arr):
    minPrice=float('inf')
    maxProfit=0
    for i in range(len(arr)):
        if arr[i]<minPrice:
            minPrice=arr[i]
        elif arr[i]-minPrice>maxProfit:
            maxProfit=arr[i]-minPrice
    return maxProfit


arr=[7,2,5,1,6,4,1]
profit=prediction(arr)
print("Your profit is: ",profit)