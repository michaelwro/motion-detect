# MOTION DETECTOR  

This is a quick code I made to catch my roomate snooping around my room while I was away at class. It worked perfectly!

Use OpenCV and a camera to detect motion.
Uses the difference between consecutive video frames to detect motion. Inspired by a [tutorial from Intel](https://software.intel.com/en-us/node/754940)

Author: **Michael Wrona** | B.S. Aerospace Engineering


## HOW TO RUN

There are a few 'argv' options for users to use. The user can specify a delay time before the motion detection begins, so the user can exit the room. The camera number that OpenCV uses can also be specified. When motion is captured, an image file is created with the date and time, within a folder with the current date.

### Specify Delay Time
* Example: To delay the motion detector by 10 seconds. Uses default OpenCV camera `0`.

`$ python main.py 10`

### Specify Delay Time & Camera Number

A laptop/internal camera will be camera 0. If an external webcam is plugged in, the built-in camera is 1, and the webcam is 0.

* Example: Delay of 30 seconds, use laptop internal camera
    * `$ python main.py 30 0`

* Example: Delay of 30 seconds, use webcam on desktop (no internal camera)
    * `$ python main.py 30 0`

* Example: Delay of 30 seconds, use external webcam plugged into laptop
    * `$ python main.py 30 0`
