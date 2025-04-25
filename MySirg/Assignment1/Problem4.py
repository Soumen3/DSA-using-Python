n=int (input("Enter the value of n: "))

lst=[]
num=2
count=0
while 1:
    for i in range(num//2+1):
        if num%2==0:
            break
    else:
        lst.append(num)
        count+=1
    num+=1

    if count >=n:
        break

print(f"The first {n} number of prime numbers are: ", lst)