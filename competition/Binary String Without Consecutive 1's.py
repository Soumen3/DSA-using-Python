def string(x):
    zeroend=1   # '0'
    oneend=1    # '1'
    sum=zeroend+oneend

    if x==1: return sum
    else:
        for i in range(2,x+1):
            oneend=zeroend
            zeroend=sum
            sum=zeroend+oneend
    return sum


x=5
print("The number of strins are: ",string(x))
