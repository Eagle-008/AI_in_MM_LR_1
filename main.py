import pylab
pylab.rcParams['figure.figsize'] = (16.0, 8.0)

from process_video import process_video
from find_global_centroid import find_global_centroid

MAX_CONTOURS_DETECTING = 2                                         # Какое число выделенных контуров используется в вычислении координат метки.
MARKING_PERIOD         = 5                                         # В кадрах. Раз в какое число кадров они анализируются и ставятся метки.
NEW_OBJECT_GAP         = 2                                         # В кадрах. Сколько анализируемых кадров подряд должно пройти, чтобы изменился цвет маркеров.
INPUT_FILE             = '.\\content\\worker-zone-detection1Trim.mp4'    # Путь к исходному файлу
OUTPUT_FILE            = 'result.mp4'                              # Путь к новому файлу
LOWER_COLOR            = (190, 50 ,10)                             # Нижняя граница искомого цвета
HIGHER_COLOR           = (254, 126, 90)                            # Верхняя граница искомого цвета
COLORS                 = [(150,224,208), (220, 20, 60), (173, 255, 47), (127, 255, 212), (255, 140, 0), (238, 130, 238), (30, 144, 255)]

def main():
  process_video(INPUT_FILE, OUTPUT_FILE, COLORS, LOWER_COLOR, HIGHER_COLOR, MAX_CONTOURS_DETECTING, NEW_OBJECT_GAP, MARKING_PERIOD)

if __name__ == '__main__':
  main()