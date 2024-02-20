import cv2

# loading pandas and numpy
import pandas as pd
import numpy as np

img = cv2.imread('test.jpg')    # return numpy array (rgba channel)
cv2.imshow('Image Show', img)
cv2.waitKey(0)

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)      # return num array (gray)
cv2.imshow('Image Show', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

df = pd.DataFrame(np.concatenate(img))     # return dataframe
print(df)
