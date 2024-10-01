import cv2
from detect_color import detect_color
from draw_markers_history import draw_markers_history

def process_video(input_file, output_file, colors, lower_color, higher_color, max_contours_detecting, new_object_gap, marking_period):
  cap = cv2.VideoCapture(input_file)

  writer = cv2.VideoWriter(output_file,                          # путь к файлу
                          cv2.VideoWriter_fourcc(*'MP4V'),       # кодек
                          round(cap.get(cv2.CAP_PROP_FPS)),      # FPS
                          (int(cap.get(3)),int(cap.get(4)))      # разрешение
                          )

  print("Total Frames:", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
  print("FPS detected:", round(cap.get(cv2.CAP_PROP_FPS)))


  new_object_frames_count = 0
  markers_history = []
  color_id = 0
  batch_counter = 0
  frames_counter = 0
  total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


  ret, frame_bgr = cap.read()
  while ret:
    frames_counter += 1
    batch_counter += 1
    if frames_counter % int(total_frames * 0.1) == 0:
        print("Progress: {0}0%".format(frames_counter // int(total_frames * 0.1)))

    if batch_counter == marking_period:
      batch_counter = 0
      coords = detect_color(frame_bgr, lower_color, higher_color, max_contours_detecting)
      if coords:
        if new_object_frames_count > new_object_gap:
          color_id += 1
        new_object_frames_count = 0
        markers_history.append({"coordinates": coords, "color": colors[color_id % len(colors)]})
      else:
        new_object_frames_count += 1
    frame_bgr = draw_markers_history(frame_bgr, markers_history)
    writer.write(frame_bgr)
    ret, frame_bgr = cap.read()
  writer.release()