import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('video.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
success, frame = cap.read()
success = True
while(success):
    min = 3600
    # Capture frame per minute (currentFrame*3600)
    cap.set(cv2.CAP_PROP_POS_MSEC,(currentFrame*min))
    success, frame = cap.read()
    # Saves image of the current frame in jpg file
    print('Read a new frame: ', success)
    if(success != False):
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        currentFrame += 1
    # To stop duplicate images
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()