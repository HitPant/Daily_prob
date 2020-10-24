'''
this program ge t a string from the user and prints the maximum occuring word
'''


#get the string from the user
sent= input("Enter a sentence: ")

#print original sent
print(sent)

#define an empty dict
freq= {}
#convert string to sent
sent= list(sent.split(" "))
#iterate through the list
for i in sent:
    #check the count in empty dict
    # if present +1
    if i in freq:
        freq[i] += 1
    #else if first occurance
    else:
        freq[i] = 1

# print(freq)
#get the max from the
res= max(freq, key= freq.get)
#print the max word
re= (max(freq.values()))

print(f"Max_word: {res} count {re}")
