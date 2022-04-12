import os

from PIL import Image

# Crops the image and saves it as "new_filename"
def crop_image(img, crop_area, new_filename):
    cropped_image = img.crop(crop_area)
    cropped_image.save(new_filename)

# The x, y coordinates of the areas to be cropped. (x1, y1, x2, y2)
crop_areas = [(180, 242, 330, 566), (340, 150, 900, 570)]

image_name = '/home/alervice/Desktop/output_videos/00001.jpg'
img = Image.open(image_name)

# Loops through the "crop_areas" list and crops the image based on the coordinates in the list
for i, crop_area in enumerate(crop_areas):
    filename = os.path.splitext(image_name)[0]
    ext = os.path.splitext(image_name)[1]
    new_filename = filename + '_cropped' + str(i) + ext

    crop_image(img, crop_area, new_filename)