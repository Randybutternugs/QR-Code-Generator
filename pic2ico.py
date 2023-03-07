#!/usr/local/bin/python3
from PIL import Image
import os
 
# Open The Image to PIXELIZE
img = Image.open("Ham.webp")
 
# The smallest is the resize, the biggest are the PIXELS
# imgSmall = img.resize((128, 128), resample=Image.BILINEAR)
# If you do want ANTIALISING uncomment the line above and comment the one below
imgSmall = img.resize((256, 256))
 
# Scale back up using NEAREST to original size
result = imgSmall.resize(img.size,Image.NEAREST)
 
# Save the image as an .ico file
result.save('yesy.ico', format='ICO')



