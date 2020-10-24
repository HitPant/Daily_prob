'''
usage:
this program is for extracting the values from the dictionary
'''

#get the key word
temp= input("Enter the field to extract: ")

#initialize a dictionary
employee = {"emp1": {"Name": "Harry","Dept": "Developer", "id": 15},
            "emp2": {"Name": "Jack","Dept": "Ops", "id": 166},
            "emp3": {"Name": "Lis", "Dept": "sales", "id": 343}}


#iterate through the dictionary
for key, val in employee.items():
    #find the key word in the val
    if temp in val:
        #get the value
        op= val[temp]
        print(str(op))
