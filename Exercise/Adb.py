import os
import sys

command = "adb logcat"
logcat = os.popen(command)

while True:
    data = logcat.readline()
    if "music" in data:
        print("##########3"+data)
    if "camera" in data:
        print("%%%%%%%%%"+data)
