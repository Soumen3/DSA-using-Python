
def three_sum(arr):
    arr.sort()
    results=[]
    for i in range (len(arr)):
        k=i+1
        l=len(arr)-1
        while k<l:
            if arr[k]+arr[l]==-(arr[i]):
                if [arr[i],arr[k],arr[l]] not in results:
                    results.append([arr[i],arr[k],arr[l]])
                k+=1
                l-=1
            elif arr[k]+arr[l] > -(arr[i]):
                l-=1
            else:
                k+=1
    return results
    

arr=[-1,0,1,2,-1,-4]
res=three_sum(arr)
print(res)