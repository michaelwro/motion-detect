"""MotionDetectFuncts.py
===============================================================================
                                MOTION DETECTOR                                    
===============================================================================
Use OpenCV and a camera to detect motion. Uses the difference between 
consecutive video frames to detect motion. Inspired by a tutorial from Intel:
https://software.intel.com/en-us/node/754940

SEE README.md for instructions on how to use project

Author: Michael Wrona

"""


import os
import cv2
import sys
import time
import datetime
import numpy as np


def euclidean_distance(frame1, frame2):
    """EUCLIDIAN DISTANCE
    Calculate the Euclidian distance between two 3D arrays
    https://en.wikipedia.org/wiki/Euclidean_distance

    @param <frame1>     First BGR image
    @param <frame2>     Second BGR image
    @type <frame1>      numpy.ndarray (3D color)
    @type <frame2>      numpy.ndarray (3D color)
    @return <eucDist>   Euclidian distance between images
    @rtype <eucDist>    numpy.ndarray (2D grayscale)
    """
    # Convert images to 32-bit data type
    img1 = np.float32(frame1)
    img2 = np.float32(frame2)

    # Compute/return Euclidian distance
    return np.sqrt(
        ((img1[:, :, 0] - img2[:, :, 0]) ** 2)
        + ((img1[:, :, 1] - img2[:, :, 1]) ** 2)
        + ((img1[:, :, 2] - img2[:, :, 2]) ** 2)
    )


def save_image(folder, img, num):
    """Save and timestamp an image
    
    @param <folder> Place to store images.
    @param <img>    Image to save
    @param <num>    How many images have been captured.
    @type <folder>  str
    @type <img>     numpy.ndarray (2D grayscale)
    @type <num>     int
    """
    now = datetime.datetime.now()   # Get date/time info

    print("Smile, you\'re on camera!\tEVENT CAPTURED: %d:%d:%d" % (now.hour, now.minute, now.second))

    imgTitle = "%d_%d_%d-%d" % (now.hour, now.minute, now.second, num)
    imgSave =  folder + str("\\") + imgTitle + str(".jpg")
    cv2.imwrite(imgSave, img)


def wait_to_clear_room(delay):
    """Wait a certain time for the user to exit the room.
    Use sys.argv to determine the wait time in seconds

    @param <delay>  Time delay [s]
    @type <delay>   str
    """
    print("Waiting to clear room...")

    delayInt = int(delay)
    for timeLeft in range(delayInt, 0, -1):
        print(timeLeft, sep="", end=" ", flush=True)
        time.sleep(1)
