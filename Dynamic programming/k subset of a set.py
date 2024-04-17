def subset(n,k):
    if n==1 or k==n:
        return 1
    return (k * subset(n-1,k) + subset(n-1,k-1))

n = 4  # number of element in the set
k = 2  # number of subset
print("the number of ways to divide the set into subset: ",subset(n,k))


# -------------------PROGRAM IS WRONG---------------#