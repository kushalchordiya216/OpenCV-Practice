# %%
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(
    'D:/UI Customization/Wallpapers/Cyberpunk/purple_cyberpunk1.jpg')
cv2.imshow('original', img)
plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
