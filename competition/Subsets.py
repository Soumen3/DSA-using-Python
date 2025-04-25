def get_poset(arr):
    poset=[]
    noOfSet=1<<len(arr)

    for i in range(noOfSet):
        subset=[]
        for j in range(len(arr)):
            if i & (1<<j):
                subset.append(arr[j])
        poset.append(subset)

    return poset


if __name__=="__main__":
    arr=[1,2,3]
    print(get_poset(arr))