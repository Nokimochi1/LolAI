import cv2 as cv
import numpy as np
import os
from time import time
from windowCapture import WindowCapture
from vision import Vision
from hsvFilter import HsvFilter

wincap  = WindowCapture("League of Legends (TM) Client")
minion = Vision("minion.png")
enemyMinion = Vision("enemy.png")
minion.init_control_gui()

#hsv_filter = HsvFilter()

loop_time = time()
while True:
   

   screenshot = wincap.get_screenshot()
   #wyjscie = zFiltrami  = minion.use_hsv_filter(screenshot)
   rectangles = minion.find(screenshot, 0.4)
   
   wyjscie  = minion.draw_rectangles(screenshot, rectangles, "green")
   

   cv.imshow("Liga", wyjscie)

   print("FPS {}".format(1 / (time() - loop_time)))
   loop_time = time()

   if cv.waitKey(1) == ord("q"):
      cv.destroyAllWindows() 
      break

