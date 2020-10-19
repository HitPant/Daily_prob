'''
usage:
This script first checks the count of files in the folder,
if the count is 1 and the extension is json > it renames the file and reads it.
if the file count is more than 1 then it deletes the first file and renames the new file and reads it
until the count increases.
files are deleted based on the time of creation(oldest file among the two is deleted)
'''



#importing required libries
import os
import json
import time

#path to directory containig json file
dir= "/home/foss/Desktop/json"


#function for renaming and reading the json file
def json_process(files):
    # looping through the directory
    for fl in files:
        #checking if only 1 file is present and the extension is .json
        if len(files) == 1 and fl.endswith(".json"):

            #renaming the json file
            #scr: the original file and dist: renamed file destination
            scr = "/home/foss/Desktop/json" + "/" + fl
            dist = "/home/foss/Desktop/json" + "/" + "cameraconfig.json"
            os.rename(scr, dist)

            with open(dist, 'r') as json_file:
                data = json.load(json_file)
                clean_data= data.split(",")
            print(json.dumps(clean_data, indent=5))

        else:
            print("check file!!!")

            #just for pausing
            # time.sleep(5)

flg= True
#using while to run continuously
while True:
    files = os.listdir(dir)
    try:

        if len(files) == 1 and flg:
            #calling the function to process the file
            json_process(files)
            flg=False

        #checking the count of files in the directory
        elif len(files) > 1 and not flg:
            #removing the oldest file based on the time of creation
            delfile = min(files, key=lambda p: os.path.getctime(os.path.join(dir, p)))
            delete = os.path.join(dir, delfile)
            os.remove(delete)
            flg = True

    #handling the error
    except Exception as e:
        print("error in except", e)
        pass




