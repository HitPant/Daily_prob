
A = [[12,7],
    [4 ,5]]

B = [[5,4],
    [6,7]]


result = [[0,0],
         [0,0]]

#loop over rows of A(len=3)
for i in range(len(A)):
    #loop over column of B(len=4)
   for j in range(len(B[0])):
       #loop over the rows of B(len=3)
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]
           # print(result)

for i in result:
    print(i)

