import cv2 as cv
import numpy as np
import os
from time import time
from windowCapture import WindowCapture
from vision import Vision

wincap  = WindowCapture("League of Legends (TM) Client")
blueBuff = Vision("minion.png")

loop_time = time()
while True:
   
   screenshot = wincap.get_screenshot()
   
   points = blueBuff.find(screenshot, 0.35, "rectangles")
   #cv.imshow("Liga", screenshot)

   print("FPS {}".format(1 / (time() - loop_time)))
   loop_time = time()

   if cv.waitKey(1) == ord("q"):
      cv.destroyAllWindows() 
      break
