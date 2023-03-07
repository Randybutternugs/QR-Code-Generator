from PIL import Image

# Define the pixel data for the image
pixels = [
    0,0,0,0,0,0,0,0,
    0,255,0,0,0,255,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,255,255,255,255,255,255,0,
    0,255,0,0,0,255,0,0,
    0,0,255,255,255,0,0,0,
    0,0,0,0,0,0,0,0
]

# Create a 16x16 pixel image from the pixel data
img = Image.new('L', (16, 16))
img.putdata(pixels)

# Save the image as an .ico file
img.save('evsmile.ico', format='ICO')
