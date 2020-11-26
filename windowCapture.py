import win32gui, win32ui, win32con
import numpy as np

class WindowCapture:

    w = 0
    h = 0
    hwnd = None

    def __init__(self, window_name):

        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception("I can't find your window")

        self.w = 1024
        self.h = 768

    def get_screenshot(self):

       wDC = win32gui.GetWindowDC(self.hwnd)
       dcObj=win32ui.CreateDCFromHandle(wDC)
       cDC=dcObj.CreateCompatibleDC()
       dataBitMap = win32ui.CreateBitmap()
       dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
       cDC.SelectObject(dataBitMap)
       cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)

       signedIntsArray = dataBitMap.GetBitmapBits(True)
       img = np.fromstring(signedIntsArray, dtype="uint8")
       img.shape = (self.h, self.w, 4)

       dcObj.DeleteDC()
       cDC.DeleteDC()
       win32gui.ReleaseDC(self.hwnd, wDC)
       win32gui.DeleteObject(dataBitMap.GetHandle())

       img = img[...,:3]
       img = np.ascontiguousarray(img)

       return img