import cv2

# Функция нахождения геометрического центра искомых областей
def find_global_centroid(frame_threshold, max_contours_detecting):
  contours, _ = cv2.findContours(frame_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  contours = sorted(contours, key=lambda x: cv2.contourArea(x))
  contours = sorted(contours, key=cv2.contourArea,reverse=True)

  contours_info = []
  total_area = 0
  centerX = 0
  centerY = 0

  if len(contours) > 0:
    for cnt in contours[:min(len(contours), max_contours_detecting)]: # Использование глобальных переменных!
        area = cv2.contourArea(cnt)
        moments = cv2.moments(cnt)

        if moments["m00"] != 0:
          cx = int(moments["m10"] / moments["m00"])
          cy = int(moments["m01"] / moments["m00"])
        else:
          cx, cy = 0, 0

        contours_info.append({"area": area, "cx": cx, "cy": cy})
        total_area += area

    if total_area > 0:
      for cnt in contours_info:
        centerX += cnt["area"]/total_area * cnt["cx"]
        centerY += cnt["area"]/total_area * cnt["cy"]
      centerX = round(centerX)
      centerY = round(centerY)

    return (centerX, centerY)
  return None