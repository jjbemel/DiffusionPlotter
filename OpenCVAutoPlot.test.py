import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('B:\Capstone Proj\Capt2\Export\February 2 T1 min (600).jpg',0)

minimum = min(img.flatten())
maximum = max(img.flatten())
print("Shape: "+str(img.shape))
print("Min= "+str(minimum)+", Max= "+str(maximum))
i,j = np.where(img == minimum)
row = i[0]
col = j[0]

with open('pixlen.txt') as f:
    length = f.readline()
    length = length.rstrip('\n')
    length = float(length) / 5

print(length)
x = np.arange(img.shape[1])/length
print(x)
y = img[row][:]
print(y)

print(float(length))

print(min(img[row][:]))
print(min(img[:][col]))

plt.plot(x,y)
plt.show()
