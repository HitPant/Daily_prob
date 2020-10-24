'''
this program is for checking the camera health that is, if the sources
are streaming output or not.
In this script there are 2 sources for which all the combinations are checked.
'''

#import library
import cv2



#get the camera sources
vcap1= cv2.VideoCapture("rtsp://admin:123Landmark@203.88.155.102:3936/Streaming/Channels/101")
vcap2= cv2.VideoCapture("rtsp://admin:123Landmark@203.88.155.102:3936/Streaming/Channels/103")

#set flag value as false
cam_check= False

#loop until true
while True:
    try:
        #if source 1 is giving output and source 2 is giving output
        if vcap1.isOpened() == True and vcap2.isOpened() == True and cam_check == False:
            print("Camera_Status:")
            print("cam1: True")
            print("cam2: True")
            # change flag status
            cam_check = True

        # if source 1 is not giving output and source 2 is not giving output
        if vcap1.isOpened() == False and vcap2.isOpened() == False and cam_check == False:
            print("Camera_Status:")
            print("cam1: False")
            print("cam2: False")
            # change flag status
            cam_check = True

        # if source 1 is giving output and source 2 is not giving output
        if vcap1.isOpened() == True and vcap2.isOpened() == False and cam_check == False:
            print("Camera_Status:")
            print("cam1: True")
            print("cam2: False")
            #change flag status
            cam_check = True

        # if source 1 is giving output and source 2 is not giving output
        if vcap1.isOpened() == False and vcap2.isOpened() == True and cam_check == False:
            print("Camera_Status:")
            print("cam1: False")
            print("cam2: True")
            # change flag status
            cam_check = True

    except:
        print("check!!")
        pass


