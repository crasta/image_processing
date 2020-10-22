#!/usr/bin/env python3
"""
How to create an image
"""

import cv2
import time
import numpy as np
import random
from sys import platform



def main():
    print("[INFO] opening the caamera ...")
    vid = cv2.VideoCapture(0)
    time.sleep(2.0)
    fps = 30
    frame_width, frame_height = 640, 480
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    vid.set(cv2.CAP_PROP_FPS, fps)

    codec = 'XVID'
    out = './output_webcam.avi'
    fps = 20 #cv2.get(cv2.CAP_PROP_FPS)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    thickness = 1
    fourcc = cv2.VideoWriter_fourcc(*codec)
    writer = None
    h, w = (None, None)
    R = (0, 0, 255)
    G = (0, 255, 0)
    B = (255, 0, 0)
    W = (255, 255, 255)
    K = (0, 0, 0)
    radius = int(5) # integer
    frame_count = 0

    while vid.isOpened():
        # Conventions: opencv uses BGR contrary to RGB
        ret, frame = vid.read()
        frame_count += 1
        if writer is None:
            h, w, _ = frame.shape
            writer = cv2.VideoWriter(out, fourcc, fps, (2*w, 2*h))
            zeros = np.zeros((h,w), dtype="uint8")
            y_start_point = (w//2, 0)
            x_start_point = (0, h//2)
            y_end_point = (w//2, h)
            x_end_point = (w, h//2)
            org = (w//2, h//2)

        b, g, r = cv2.split(frame)
        r = cv2.merge([zeros, zeros, r])
        g = cv2.merge([zeros, g, zeros])
        b = cv2.merge([b, zeros, zeros])

        out = np.zeros((2*h, 2*w, 3), dtype="uint8")
        out[0:h, w:2*w] = r
        out[h:2*h, w:2*w] = g
        out[h:2*h, 0:w] = b

        cv2.line(frame, y_start_point, y_end_point, W, thickness)
        cv2.line(frame, x_start_point, x_end_point, W, thickness)
        cv2.circle(frame, org, radius, W, -1)
        cv2.putText(frame, '(0,0)', tuple(np.array(org) + np.array((3,-10))), font, fontScale, W, thickness, cv2.LINE_AA)
        cv2.circle(frame, org, 240, B, thickness)
        if frame_count % 25 == 0:
            m = min(w,h)
            x0 = random.randint(m/2-150, m/2+150)
            y0 = random.randint(m/2-150, m/2+150)
            x1 = x0 + 25
            y1 = y0 + 25
            cv2.rectangle(frame, (x0, y0), (x1, y1), K, -1)
            cv2.line(frame, org, ( (x0+x1)//2, (y0+y1)//2), K, thickness)
        out[0:h, 0:w] = frame

        writer.write(out)

        cv2.imshow("Output", out)
        cv2.resize(out, (400, 400))

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print()
            print("[WARNING] pressed q button...")
            print()
            break

    print("[INFO] cleaning up ....")
    print()
    cv2.destroyAllWindows()
    writer.release()
    vid.release()


if __name__=="__main__":
    print("[INFO] checking for linux OS platform ...")
    print()
    if platform.lower() in {"linux", "linux2"}:
        if not cv2.useOptimized():
            cv2.setUseOptimized(True)
        main()
    elif platform.lower() in {"darwin", "win32"}:
        print("Not a linux platform ...")
        exit()
