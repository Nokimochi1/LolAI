import cv2 as cv
import numpy as np
import os
from time import time
from windowCapture import WindowCapture


wincap = WindowCapture("League of Legends (TM) Client")

loop_time = time()
while True:

   screenshot = wincap.get_screenshot()

   cv.imshow("tak to widze", screenshot)

   print('FPS {}'.format(1 / (time() - loop_time)))
   loop_time = time()

   if cv.waitKey(1) == ord("q"):
      cv.destroyAllWindows() 
      break

print("done")
      
