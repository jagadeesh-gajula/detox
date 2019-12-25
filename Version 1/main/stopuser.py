import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import ImageGrab
import ctypes
import os
import time
from win10toast import ToastNotifier

model = load_model('nsfw.h5')
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

def action():
    toaster = ToastNotifier()
    res=toaster.show_toast("Content warning","\n Please close the content or system will lock")
    if res==1:
        time.sleep(10)
        if scanner()==1:
            ctypes.windll.user32.LockWorkStation()

def scanner():
        snapshot = ImageGrab.grab()
        snapshot.save("admin.jpg")
        test_image = image.load_img('admin.jpg', target_size = (64, 64)) 
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        return result
        os.system('del admin.jpg')

while True:
    if scanner() == 0:
        print("scanning")
    if scanner()== 1:
        print("taking action")
        action()