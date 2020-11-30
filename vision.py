import cv2 as cv
import numpy as np
from hsvFilter import HsvFilter

class Vision:

    TRACKBAR_WINDOW = "Trackbars"
    szukana = None
    szukana_w = 0
    suzkana_h = 0
    method = None
    color = None


    # Typy metod szukania https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
    def __init__(self, szukana_path, method=cv.TM_CCOEFF_NORMED):
        

        self.szukana = cv.imread(szukana_path, cv.COLOR_RGB2BGR)

        self.szukana_w = self.szukana.shape[1]
        self.szukana_h = self.szukana.shape[0]

        self.method = method

    def find(self, obraz, threshold=0.5, debug_mode=None):

        result = cv.matchTemplate(obraz, self.szukana, self.method)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.szukana_w, self.szukana_h]
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        return rectangles


    def click_position(self, rectangles):

        points = []

        for (x, y, w, h) in rectangles:

            center_x = x + int(w/2)
            center_y = y + int(h/2)

            points.append((center_x, center_y))

        return points


    def draw_rectangles(self, obraz, rectangles, color="green"):


        if color == "green":
            line_color = (0, 255, 0)
            line_type  = cv.LINE_4

        elif color == "red":
            line_color = (0, 0, 255)
            line_type  = cv.LINE_4

        elif color == "blue":
            line_color = (255, 0, 0)
            line_type  = cv.LINE_4


        for (x, y, w, h) in rectangles:

            top_left = (x, y)
            bottom_right = (x + w, y + h)

            cv.rectangle(obraz, top_left, bottom_right, color=line_color, lineType=line_type, thickness=2)

        return obraz


    def draw_crosses(self, obraz, points, color="green"):


        if color == "green":
            cross_color = (0, 255, 0)
            cross_type  = cv.MARKER_CROSS

        elif color == "red":
            cross_color = (0, 0, 255)
            cross_type  = cv.MARKER_CROSS

        elif color == "blue":
            cross_color = (255, 0, 0)
            cross_type  = cv.MARKER_CROSS

        for (center_x, center_y) in points:

            cv.drawMarker(obraz, (center_x, center_y), marker_color, marker_type)

        return obraz

    def init_control_gui(self):


        cv.namedWindow(self.TRACKBAR_WINDOW, cv.WINDOW_NORMAL)
        cv.resizeWindow(self.TRACKBAR_WINDOW, 350, 700)

        # To dodałem bo musi przyjać jakąś funkcje jako argument
        def nothing(position):
            pass


        # Kod z dokumentacji OpenCV
        # create trackbars for bracketing.
        # OpenCV scale for HSV is H: 0-179, S: 0-255, V: 0-255
        cv.createTrackbar('HMin', self.TRACKBAR_WINDOW, 0, 179, nothing)
        cv.createTrackbar('SMin', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('VMin', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('HMax', self.TRACKBAR_WINDOW, 0, 179, nothing)
        cv.createTrackbar('SMax', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('VMax', self.TRACKBAR_WINDOW, 0, 255, nothing)
        # Set default value for Max HSV trackbars
        cv.setTrackbarPos('HMax', self.TRACKBAR_WINDOW, 179)
        cv.setTrackbarPos('SMax', self.TRACKBAR_WINDOW, 255)
        cv.setTrackbarPos('VMax', self.TRACKBAR_WINDOW, 255)

        # trackbars for increasing/decreasing saturation and value
        cv.createTrackbar('SAdd', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('SSub', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('VAdd', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('VSub', self.TRACKBAR_WINDOW, 0, 255, nothing)

    def get_hsv_filter_from_controls(self):

        # Tworzy instancje HsvFilter i podaje wartosci z okna z gui (w skrocie)
        hsv_filter = HsvFilter()
        hsv_filter.hMin = cv.getTrackbarPos('HMin', self.TRACKBAR_WINDOW)
        hsv_filter.sMin = cv.getTrackbarPos('SMin', self.TRACKBAR_WINDOW)
        hsv_filter.vMin = cv.getTrackbarPos('VMin', self.TRACKBAR_WINDOW)
        hsv_filter.hMax = cv.getTrackbarPos('HMax', self.TRACKBAR_WINDOW)
        hsv_filter.sMax = cv.getTrackbarPos('SMax', self.TRACKBAR_WINDOW)
        hsv_filter.vMax = cv.getTrackbarPos('VMax', self.TRACKBAR_WINDOW)
        hsv_filter.sAdd = cv.getTrackbarPos('SAdd', self.TRACKBAR_WINDOW)
        hsv_filter.sSub = cv.getTrackbarPos('SSub', self.TRACKBAR_WINDOW)
        hsv_filter.vAdd = cv.getTrackbarPos('VAdd', self.TRACKBAR_WINDOW)
        hsv_filter.vSub = cv.getTrackbarPos('VSub', self.TRACKBAR_WINDOW)
        return hsv_filter

    def use_hsv_filter(self, original_image, hsv_filter=None):

        hsv = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)


        # Gdy filtr nie jest podany bierzemy go z gui
        if not hsv_filter:
            hsv_filter = self.get_hsv_filter_from_controls()

        h, s, v = cv.split(hsv)
        s = self.shift_channel(s, hsv_filter.sAdd)
        s = self.shift_channel(s, -hsv_filter.sSub)
        v = self.shift_channel(v, hsv_filter.vAdd)
        v = self.shift_channel(v, -hsv_filter.vSub)
        hsv = cv.merge([h, s, v])

        # Ustawiamy minimalne i maksymalne wartosci jakie chcemy wyswietlic
        lower = np.array([hsv_filter.hMin, hsv_filter.sMin, hsv_filter.vMin])
        upper = np.array([hsv_filter.hMax, hsv_filter.sMax, hsv_filter.vMax])

        # Uzywamy filtru na obraz
        maska = cv.inRange(hsv, lower, upper)
        result = cv.bitwise_and(hsv, hsv, mask=maska)

        # Znowu zmieniamy na BGR zeby wszystko pokazywało sie dobrze
        img = cv.cvtColor(result, cv.COLOR_HSV2BGR)

        return img

    # https://stackoverflow.com/questions/49697363/shifting-hsv-pixel-values-in-python-using-numpy
    def shift_channel(self, c, amount):
        if amount > 0:
            lim = 255 - amount
            c[c >= lim] = 255
            c[c < lim] += amount
        elif amount < 0:
            amount = -amount
            lim = amount
            c[c <= lim] = 0
            c[c > lim] -= amount
        return c
