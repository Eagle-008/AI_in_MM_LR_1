import cv2

# Примечание: здесь можно сделать хорошую оптимизацию, если не каждый раз отрисовывать все маркеры, а сделать отдельный фрейм с маркерами и маску,
# и накладывать это на кадры основго видео. При этом при добавлении новых маркеров, добавлять их один раз на фрейм с  маской.
def draw_markers_history(frame_bgr, marker_history):
  frame_RGB = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

  for marker in marker_history:
    if marker["coordinates"]:
      thickness = 3
      marker_size = 25
      cv2.drawMarker(frame_RGB, marker["coordinates"], color=marker["color"], thickness=thickness,
        markerType= cv2.MARKER_TILTED_CROSS, line_type=cv2.LINE_AA,
        markerSize=marker_size)

  return cv2.cvtColor(frame_RGB, cv2.COLOR_RGB2BGR)