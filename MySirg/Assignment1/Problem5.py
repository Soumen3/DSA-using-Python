n=int(input("Enter the vlaue of n: "))
lst=[]
first,second=0,1

for i in range(n):
    lst.append(first)
    first,second=second,first+second

print("The fobonacci serise is: ",lst)