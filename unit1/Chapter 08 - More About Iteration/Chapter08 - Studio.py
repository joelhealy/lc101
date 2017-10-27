import image
import sys
import random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        # Randomly choose the coordinates of a neighboring pixel
        old_p = img.getPixel(i + random.randrange(-1, 2), j + random.randrange(-1, 2))
        # In the new image, set this pixel's color to the neighbor's color
        new_img.setPixel(i, j, old_p)
new_img.draw(win)
win.exitonclick()
