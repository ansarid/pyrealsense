import pyrealsense as pyrs
import matplotlib.pyplot as plt

pyrs.start()
dev = pyrs.Device()  #ivcam_preset = pyrs.cnst.rs_ivcam_preset.RS_IVCAM_PRESET_GESTURE_RECOGNITION

import time
import matplotlib.pyplot as plt
import pyrealsense as pyrs
pyrs.start()
time.sleep(2)

dev.wait_for_frame()
cm = dev.colour
plt.imshow(cm)
plt.show()

import cv2
import numpy as np

cnt = 0
last = time.time()
smoothing = 0.9;
fps_smooth = 30

while True:

    cnt += 1
    if (cnt % 10) == 0:
        now = time.time()
        dt = now - last
        fps = 10/dt
        fps_smooth = (fps_smooth * smoothing) + (fps * (1.0-smoothing))
        last = now

    dev.wait_for_frame()
    c = dev.colour
    c = cv2.cvtColor(c, cv2.COLOR_RGB2BGR)
    d = dev.depth >> 3
    d = cv2.applyColorMap(d.astype(np.uint8), cv2.COLORMAP_RAINBOW)

    cd = np.concatenate((c,d), axis=1)

    cv2.putText(cd, str(fps_smooth)[:4], (0,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0))

    cv2.imshow('', cd)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
