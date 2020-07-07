"""main.py
===============================================================================
                                MOTION DETECTOR                                    
===============================================================================
Use OpenCV and a camera to detect motion. Uses the difference between 
consecutive video frames to detect motion. Inspired by a tutorial from Intel:
https://software.intel.com/en-us/node/754940

SEE README.txt for instructions on how to use project

Author: Michael Wrona

"""


import os
import cv2
import sys
import time
import datetime
import numpy as np
from motionDetect import MotionDetectFuncts

# DEFINE GLOBAL CONSTANTS
STD_THRESHOLD = 21.5
IMG_GAIN = 1.3


def main():
    # Create folder for captured images
    now = datetime.datetime.now()
    dataFolderName = "%d-%d-%d" % (now.month, now.day, now.year)
    dataFolder = os.getcwd() + str("\\output\\") + dataFolderName
    os.mkdir(dataFolder)

    if len(sys.argv) == 1:
        # If no arguments are given
        cap = cv2.VideoCapture(0)  # Initialize capture
    elif len(sys.argv) == 2:
        # If time-delay arguments is given
        cap = cv2.VideoCapture(0)  # Initialize capture
        MotionDetectFuncts.wait_to_clear_room(sys.argv[1])
    elif len(sys.argv) == 3:
        # If time-delay and camera input are given
        MotionDetectFuncts.wait_to_clear_room(sys.argv[1])
        cap = cv2.VideoCapture(int(sys.argv[2]))  # Initialize capture
    else:
        # If nothing is given
        cap = cv2.VideoCapture(0)  # Initialize capture


    # Capture initial frames
    _, frame1 = cap.read()
    _, frame2 = cap.read()
    
    currImgNum = 1

    # Capture video
    while True:
        _, frame3 = cap.read()
        rows, cols, _ = np.shape(frame3)

        # Calculate difference
        diff = MotionDetectFuncts.euclidean_distance(frame1, frame3)

        frame1 = frame2  # Swap frames
        frame2 = frame3

        blurred = cv2.GaussianBlur(diff, (5, 5), 0.1) * IMG_GAIN  # Blur image
        _, threshed = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)  # Threshold image
        stdDev = np.std(threshed)  # Calculate std. deviation

        """DISPLAY RESULTS
        Uncomment for viewing different data:
        Option 1 - Raw output from camera
        Option 2 - Difference plot, normalized to [0, 1]
        Option 3 - Thresholded image [0, 1]
        Option 4 - Standard deviation value. Use to tune threshold for motion detection
        """
        cv2.imshow("Output - From Camera", frame1)  # Option 1
        # cv2.imshow(
        #     "Output - Difference (Normalized)", diff / np.sqrt(255**2 + 255**2 + 255**2)
        # )  # Option 2
        # cv2.imshow("Output - Threshold Image", threshed)  # Option 3
        # print(stdDev)  # Option 4


        if stdDev > STD_THRESHOLD:
            # If motion is detected
            MotionDetectFuncts.save_image(dataFolder, frame1, currImgNum)
            currImgNum += 1
        

        # Add pause to prevent overflow of images
        time.sleep(0.5)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    now = datetime.datetime.now()
    print("Ended: %d-%d" % (now.hour, now.minute))


if __name__ == '__main__':
    main()

