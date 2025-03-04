import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import scipy.datasets as sd
from PIL import Image

matplotlib.use('TkAgg')

# 1-Dimensional Arrays (Vectors)
my_array = np.array([1.1, 9.2, 8.1, 4.7])
print(my_array.shape)
print(my_array[2])
print(my_array.ndim)

# 2-Dimensional Arrays (Matrices)
array_2d = np.array([[1, 2, 3, 9],
                     [5, 6, 7, 8]])
print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

print(array_2d[1, 2])
print(array_2d[0, :])

# N-Dimensional Arrays (Tensors)
mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])
# How many dimensions does the array below have?
print(mystery_array.ndim)
# What is its shape (i.e., how many elements are along each axis)?
print(mystery_array.shape)
# Try to access the value 18 in the last line of code.
print(mystery_array[2, 1, 3])  # -1, -1, -1 also works
# Try to retrieve a 1 dimensional vector with the values [97, 0, 27, 18]
print(mystery_array[-1, -1, :])
# Try to retrieve a (3,2) matrix with the values [[ 0, 4], [ 7, 5], [ 5, 97]]
print(mystery_array[:, :, 0])
print(mystery_array[:, :, 0].shape)

# Challenge 1: Use .arange()to create a vector a with values ranging from 10 to 29. You should get this:
a = np.arange(10, 30)
print(a)

# Create an array containing only the last 3 values of a
# [start:stop(excluded):step]
print(a[-2:])
# Create a subset with only the 4th, 5th, and 6th values
print(a[3:6])
# Create a subset of a containing all the values except for the first 12 (i.e., [22, 23, 24, 25, 26, 27, 28, 29])
print(a[12:])
# Create a subset that only contains the even numbers (i.e, every second number)
print(a[::2])

# Reverse the order of the values in 'a', so that the first element comes last
print(a[::-1])
print(np.flip(a, axis=0))

# Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]
arr = [6, 0, 9, 0, 0, 5, 0]
print([item for item in arr if item != 0])
# arr_np = np.array([6, 0, 9, 0, 0, 5, 0])
# # noinspection PyUnreachableCode
# nz_indices = np.nonzero(arr_np)
# print(nz_indices)

# Use NumPy to generate a 3x3x3 array with random numbers
rng = np.random.default_rng()
print(rng.integers(low=0, high=100, size=(3, 3, 3)))

# Use .linspace() to create a vector x of size 9 with values spaced out evenly between 0 and 100 (both included).
x = np.linspace(start=0, stop=100, num=9, dtype=int)
print(x)

# Use .linspace() to create another vector y of size 9 with values between -3 to 3 (both included).
# Then plot x and y on a line chart using Matplotlib.
y = np.linspace(start=-3, stop=3, num=9, dtype=int)
print(y)

# plt.plot(x)
# plt.plot(y)
# plt.show()

noise = rng.random(size=(128, 128, 3))
# plt.imshow(noise)
# plt.show()

# Linear Algebra with Vectors
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
print(v1 + v2)

# Python Lists vs ndarrays
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]
print(list1 + list2)

print(v1 * v2)
# print(list1 * list2)  # TypeError

# Broadcasting and Scalars

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])
print(array_2d + 10)
print(array_2d * 5)

#  Let's multiply a1 with b1.
#  Then use the .matmul() function or the @ operator to check your work.
a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

c = np.matmul(a1, b1)
print(f"Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.")
print(c)
print(a1 @ b1)

# Manipulating Images as ndarrays

img: np.ndarray = sd.face()
print(type(img))
print(img.shape)
print(img.ndim)
# plt.imshow(img)
# plt.show()
# Divide all the values by 255 to convert them to sRGB.
srgb_img = np.divide(img, 255)  # img / 255
# Multiply the sRGB array by the grey_vals array (provided) to convert the image to grayscale.
grey_vals = np.array([0.2126, 0.7152, 0.0722])
grey_img = srgb_img @ grey_vals

# plt.imshow(grey_img, cmap='gray')
# plt.show()

# You flip the grayscale image upside down
# plt.imshow(np.flip(grey_img), cmap='gray')
# plt.show()

# Rotate the colour image
# plt.imshow(np.rot90(img))
# plt.show()

# Invert (i.e., solarize) the colour image.
# To do this you need to converting all the pixels to their "opposite" value, so black (0) becomes white (255).
# plt.imshow(np.invert(img))  # 255 - img
# plt.show()

my_img = Image.open('yummy_macarons.jpg')
img_array = np.array(my_img)

print(img_array.shape)
print(img_array.ndim)
# plt.imshow(img_array)
plt.imshow(255 - img_array)
plt.show()
