'''
this program is to find if a number is palindrome or not.
a palindrome is a number that in reverse order returns the same number
ex: 111, 131,7447,......
'''

#get input fro the user
num= int(input("Enter a number: "))

#assign a temp variable
temp= num
rev_num= 0
while(num>0):

    #get the last digit of the input number
    dig= num%10
    #add to the rev digit variable
    rev_num= rev_num*10+dig
    #leave the last digit of the num and get the first 2
    num= num//10

#now check the condition for palindrome:
if(temp==rev_num):
    print("Number is palindrome")
else:
    print("Not a palindrome")
