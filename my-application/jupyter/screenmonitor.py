
# coding: utf-8

# In[9]:

import numpy as np
from keras.models import load_model
model = load_model('nsfw.h5')
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

from keras.preprocessing import image





# In[25]:

from PIL import ImageGrab
snapshot = ImageGrab.grab()
save_path = "admin.jpg"
test_image = image.load_img('admin.jpg', target_size = (64, 64)) 
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)

#predict the result
result = model.predict(test_image)
categories=['safe','not safe']
print(categories[int(result[0][0])])


# In[30]:

import os
import time
while True:
    snapshot = ImageGrab.grab()
    save_path = "admin.jpg"
    snapshot.save(save_path)
    img_path = 'admin.jpg'
    test_image = image.load_img('admin.jpg', target_size = (64, 64)) 
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    categories=['safe','not safe']
    print(categories[int(result[0][0])])
    time.sleep(1)
    os.system('del admin.jpg')

