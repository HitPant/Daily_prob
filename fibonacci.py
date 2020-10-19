'''
usage:
this program is for finding the nth fibonacci number and
print the whole series till the nth number.
ex: a fibnacci series is of the form: 0 1 1 2 3 5 8.....
the nth value is the sum of th (n-1)th and (n-2)th terms.
'''




#get the num input from the user
num= int(input("Enter a num: "))

# define the first 2 numbers of the series
n1,n2= 0,1

#set a count flag to 0
count= 0

# check if the num is less than or equal to zero
if num <= 0:
    print("Enter positive num")
#check if the num is 1
if num == 1:
    print(n1)
#else define a while loop and loop over until the condition becomes false
else:
    # while condition is true loop over
    while count < num:
        #define the first(preceding) num in each iteration
        print(n1)
        #define the next term in the series by adding the first and second term
        n_term= n1 + n2
        #update the first and second terms
        n1 = n2
        n2 = n_term
        #increase the counter
        count += 1


