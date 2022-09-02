import numpy as np
from PIL import Image
# from Pillow import Image

original_image = 'bikepic.jpg'
water_mark = 'motorcycleicon.jpg'

image = Image.open(original_image)
water_mark_image = Image.open(water_mark)

# convert to numpy arrays
image_input = np.asarray(image).copy()
water_mark_array = np.asarray(water_mark_image)
# print(water_mark_array.shape)
# print(image_input.flags)
v_offset = 1250
h_offset = 550
for i in range(0, water_mark_array.shape[0] -1):
    for j in range(0, water_mark_array.shape[1] -1):
        if water_mark_array[i][j][0] < 100:
            image_input[i + v_offset][j + h_offset] = image_input[i + v_offset][j + h_offset] + [155, 155, 155]

aaa = Image.fromarray(image_input)
aaa.show()


