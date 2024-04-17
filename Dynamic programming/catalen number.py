
# Normal method 
# def catalen(n):
#     if n<=1:
#         return 1
#     else:
#         result=0
#         for i in range(n):
#             result+= (catalen(i)*catalen(n-i-1))
#         return result
    



# Dynamic programmming
def catalen(n):
    # Base cases
    if n<=1:
         return 1
    

    # Create a memoization table to store computed Fibonacci numbers
    mem={}

     # Check if the result is already memoized
    if n in mem:
        return mem[n]
    

    # If not memoized, calculate and store the result
    result=0
    for i in range(n):
        result+=catalen(i)*catalen(n-i-1)
    mem[n]=result
    return (result)
    



# num=int(input("How many numbers you want to print: "))
num=10
for i in range(num+1):
    print(catalen(i),end=" ")
# print(mem)
