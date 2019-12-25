from PIL import ImageGrab
import time
import random

while True:
    snapshot = ImageGrab.grab()
    local_time = time.ctime(seconds)
    rand=random.random()
    save_path = string(local_time+rand)
    snapshot.save(save_path)
    print("saving your screen")


	