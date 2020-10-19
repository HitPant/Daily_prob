'''
usage:
this program is for sorting a list using insertion_sort algorithm
In this the first element is considered to be sorted and the next element is checked:
key(first value) > j(second value): if True the greater value is shifted to the right
else next to value are compared.
'''



# define a list of numbers
data = [9, 5, 1, 4, 3]

#loop in range 1 to length of the list
for i in range(1, len(data)):
    #store the unsorted value in the key variable
    key = data[i]
    # store the preceding value in j variable
    j = i - 1

    # run inside the while until the the conditions are false
    # conditions1: preceding value (j) should be greater than or equal to 0
    # conditions1: the unsorted value(key) is less than j
    while j >= 0 and key < data[j]:
        #if condition is true preceding value is put on right and key is put in preceding index
        data[j + 1] = data[j]
        j = j - 1
        #change the value in key variable and keep looping until condition is false
        data[j + 1] = key

# print the sorted list
print(data)
