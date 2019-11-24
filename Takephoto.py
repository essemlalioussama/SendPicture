from cv2 import *
import time

#returns path to photo for later use in facerec
def takeShot():
    cam = VideoCapture(0)   # 0 -> index of camera
    for i in range(5):
        s, img = cam.read()
        time.sleep(1)
    if s:    # frame captured without any errors
        imwrite("/home/essemlali/Desktop/myapp/shot.jpg",img) #save image
    cam.release()
    print("photo taken")    
    return "/home/essemlali/Desktop/myapp/shot.jpg"


