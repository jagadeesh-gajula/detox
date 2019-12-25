import PIL.ImageGrab

im = PIL.ImageGrab.grab()
MAX_SIZE = (1000,1000) 
im.thumbnail(size=MAX_SIZE)
im.save("screenshot.jpg")
im.show()