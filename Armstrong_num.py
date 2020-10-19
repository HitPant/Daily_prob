'''
usage:
this program is to find if a number is armstrong number or not
example: 153= 1^3 + 5^3 + 3^3= 1+125+27= 153
'''


#get the number from the user
num = int(input("Enter a number: "))

#initialize sum
sum = 0
temp = num
while temp > 0:
   #get the last digit of the num
   digit = temp % 10
   #get the cude of the digit
   sum += digit ** 3
   #floor division to get the first 2 numba
   temp //= 10

# check the conditions and print the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")