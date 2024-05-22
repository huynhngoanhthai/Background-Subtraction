import numpy as np
import matplotlib.pyplot as plt
import cv2

def changeBackGround(img,bg,new_bg):
    difference = np.abs(img-bg) 
    difference_binary = np.where(difference < 1, 
                                0, 255)
    output = np.where(difference_binary==0, 
                    new_bg, img)
    return output
bg_image1 = cv2.imread('images/background1.png')
bg_image2 = cv2.imread('images/background2.png')
ob_image  = cv2.imread('images/object.png')

bg_image1 = cv2.resize(bg_image1, (640, 480))
bg_image2 = cv2.resize(bg_image2, (640, 480))
ob_image  = cv2.resize(ob_image,  (640, 480))

bg_image1 = cv2.cvtColor(bg_image1, cv2.COLOR_BGR2RGB)
bg_image2 = cv2.cvtColor(bg_image2, cv2.COLOR_BGR2RGB)
ob_image  = cv2.cvtColor(ob_image,  cv2.COLOR_BGR2RGB)

output_image = changeBackGround(ob_image, bg_image1 ,bg_image2)

plt.imshow(output_image)
plt.show()