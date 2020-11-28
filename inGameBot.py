import cv2 as cv
import numpy as np
import os
from time import time
from windowCapture import WindowCapture
from vision import Vision
from hsvFilter import HsvFilter

wincap  = WindowCapture("League of Legends (TM) Client")
minion = Vision("blueBuffHsv.png")
minion.init_control_gui()

hsv_filter = HsvFilter(64, 217, 137, 119, 255, 255, 255, 24, 73, 0)

loop_time = time()
while True:
   

   screenshot = wincap.get_screenshot()
   zFiltrami = minion.use_hsv_filter(screenshot, hsv_filter)
   rectangles = minion.find(zFiltrami, 0.35)
   
   wyjscie    = minion.draw_rectangles(screenshot, rectangles)

   cv.imshow("Liga", wyjscie)

   print("FPS {}".format(1 / (time() - loop_time)))
   loop_time = time()

   if cv.waitKey(1) == ord("q"):
      cv.destroyAllWindows() 
      break
