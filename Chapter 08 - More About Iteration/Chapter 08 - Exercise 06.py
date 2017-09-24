#  Write a program to remove all the red from an image.
#
#  For this and the following exercises, use the luther.jpg photo

import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1, 15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        new_red = 0
        new_green = p.getGreen()
        new_blue = p.getBlue()

        new_pixel = image.Pixel(new_red, new_green, new_blue)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()
