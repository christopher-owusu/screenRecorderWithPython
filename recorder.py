import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics
import datetime

print("asdfghjkl"[::-1])

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_name = f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

cam = cv2.VideoCapture(0)


while True:
    img = ImageGrab.grab(bbox=(0,0, width, height))
    img_np = np.array(img)
    final_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = cam.read()
    fr_height, fr_width, _ = frame.shape
    cv2.imshow('webcam', frame)
    final_img[0:fr_height, 0:fr_width, :] = frame[0:fr_height, 0:fr_width, :]

    captured_video.write(final_img)
    cv2.imshow("Screen Recorder", final_img)
    if cv2.waitKey(10) == ord('q'):
        break