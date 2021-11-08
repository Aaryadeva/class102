import cv2
import dropbox
import time
import random

start_time=time.time()

def takeSnapshot():
    number=random.randint(0,100)
    #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frame while camera is on
        ret,frame=videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage 
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    print('Snapshot taken.')
    #releases the camera
    videoCaptureObject.release()
    #close all the windows that might be opened while this process
    cv2.destroyAllWindows()

takeSnapshot()

def uploadFile(img_name):
    access_token="psiyx8MVv30AAAAAAAAAAaEf_NBIkSb6FhxNjzzjj2Cik8j_P6BPuS75ZxpAecUt"
    file=img_name
    file_from = file
    file_to = "/testfolder/" + (img_name)
    #initialising dropbox
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time>=5)):
            name=takeSnapshot()
            uploadFile(name)

main()