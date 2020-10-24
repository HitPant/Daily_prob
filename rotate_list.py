#get the number of position user wants to shift
pos= 2

#list of numbers
nums= [1,2,4,5,66,78,9]
#get the len of the list
n= len(nums)

#iterate
for i in range(0,pos):
    #store the first element of the list in temp
    temp= nums[0]
    #iterate in the list
    for j in range(0,n-1):
        #switch the position 
        nums[j] = nums[j+1]
    #store the last element in temp
    nums[n-1]= temp
    
#for printing each number
for i in range(0,n):
    print(nums[i], end= " ")
