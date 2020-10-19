'''
usage:
this program is for finding the factorial of a given number
example factorial of 5= 1*2*3*4*5= 120
'''

#get input from the user
num= int(input("Enter a number: "))


# set a factorial flag with value equal to 1
factorial = 1

#check if the entered num is less than 0
if num < 0:
   print("Invalid")

#elif the number is equal to zero print factorial is 1
elif num == 0:
   print("factorial: 1")

# else iterate in range
else:
    # iterate in range (1 to num+1)
    for i in range(1,num + 1):
        #update the factorial value until the whole iteration
        factorial = factorial*i

#print the factorial
print("factorial: ",factorial)
