import cv2 as cv
import numpy as np

class Vision:

    szukana = None
    szukana_w = 0
    suzkana_h = 0
    method = None


    # Typy metod szukania https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
    def __init__(self, szukana_droga, method=cv.TM_CCOEFF_NORMED):
        

        self.szukana = cv.imread(szukana_droga, cv.COLOR_RGB2BGR)

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

        points = []
        if len(rectangles) > 0:

            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv.MARKER_CROSS

            for (x, y, w, h) in rectangles:

                center_x = x + int(w/2)
                center_y = y + int(h/2)
                points.append((center_x, center_y))

                if debug_mode == "rectangles":

                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    cv.rectangle(obraz, top_left, bottom_right, color=line_color, lineType=line_type, thickness=2)

                elif debug_mode == "points":
                    cv.drawMarker(obraz, (center_x, center_y), color=marker_color, markerType=marker_type, markerSize=40, thickness=2)

        if debug_mode:
            cv.imshow("Matches", obraz)


        return points
