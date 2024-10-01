import cv2
from find_global_centroid import find_global_centroid

def detect_color(frame_bgr, lower_color, higher_color, max_contours_detecting):
  frame_RGB = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
  frame_threshold = cv2.inRange(frame_RGB, lower_color, higher_color)
  coordinates = find_global_centroid(frame_threshold, max_contours_detecting)
  return coordinates