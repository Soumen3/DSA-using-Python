arr=[e for e in input("Enter the element seperated by space: ").split(' ')]
fre={}
for e in arr:
    if e in fre:
        fre[e]+=1
    else:
        fre[e]=1
print("The frequencies are:")
print(fre)

for x in fre:
    print(x,': ',fre[x])