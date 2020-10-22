#import the library
import cv2
import datetime
import os



def cam_log(log_msg):
    log_path= "./cam_logs"
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logs= open(log_path+ "/" + str(datetime.date.today()), "a+")
    logs.write(str(datetime.datetime.now()) + log_msg + "\n")
    logs.close()




#for avoiding tcp error
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"

#rtsp links
# vcap1= cv2.VideoCapture("rtsp://admin:123Landmark@203.88.155.102:3936/Streaming/Channels/101")
# vcap2= cv2.VideoCapture("rtsp://admin:123Landmark@203.88.155.102:3934/Streaming/Channels/101")

#setting flags for cam1 and cam2
cam1_stat= False
cam2_stat= False

#to run continuously
while True:

    #rtsp links
    vcap1 = cv2.VideoCapture("rtsp://admin:123Landmark@203.88.155.102:3936/Streaming/Channels/101")
    vcap2 = cv2.VideoCapture("rtsp://admin:123Landmark@203.88.155.102:3934/Streaming/Channels/102")

    try:
        # reading the frames from the link(ret1,ret2: bool and frame1,frame2: None or value )
        ret1, frame1 = vcap1.read()
        ret2, frame2 = vcap2.read()
    except:
        pass

    # if cam 1 is down
    if (not ret1 and cam1_stat):
        # change the flag value
        cam1_stat = False
        cam_status1= ("cam1: False")
        cam_log("Cam_log: " + cam_status1)
        # print(cam_status1)
    #if cam 2 is down
    if (not ret2 and cam2_stat):
        cam2_stat = False
        cam_status2= ("cam2: False")
        cam_log("Cam_logs: " + cam_status2)
        # print(cam_status2)

    #if cam1 is Up
    if (ret1 and not cam1_stat):
        #change flag value
        cam1_stat = True
        cam_status1= ("cam1: True")
        cam_log("Cam_logs: " + cam_status1)
        # print(cam_status1)
    #if cam 2 is up
    if (ret2 and not cam2_stat):
        #change flag value
        cam2_stat= True
        cam_status2= ("cam2: True")
        cam_log("Cam_logs: " + cam_status2)
        # print(cam_status2)

vcap1.release()
vcap2.release()



