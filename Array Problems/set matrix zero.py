# # ----------------------brute forse solution--------------------------------#
# def set_zero(matrix):
#     # copy_matrix=matrix[:]           # shallow copy using slice operator
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             # if the element is 0 then assing the row and column with -1
#             if matrix[i][j]==0:
#                 for k in range(len(matrix[i])):
#                     if matrix[i][k]!=0:
#                         matrix[i][k]=-1
#                 for l in range(len(matrix)):
#                     if matrix[l][j]!=0:
#                         matrix[l][j]=-1

#     # convert the -1 to 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j]==-1:
#                 matrix[i][j]=0




#--------------------Better Solution--------------------#

def set_zero(matrix):
    col=[0 for i in range(len(matrix[0]))]
    row=[0 for i in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                row[i],col[j]=1,1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0        


matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
for i in matrix:
    print(i)
set_zero(matrix)
print("The zero matrix is:")
for i in matrix:
    print(i)
