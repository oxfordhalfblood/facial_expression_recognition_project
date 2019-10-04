import numpy as np
import random
import cv2
import sys
import os
import glob

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

imageDirectory = sys.argv[1]
print(imageDirectory)
images = os.listdir(imageDirectory)
print(len(images))

img_path = glob.glob(imageDirectory + '/*.jpg')
# print(img_path[1])
for image in img_path:
    img = cv2.imread(image,0) # Only for grayscale image
    for i in range(0,9):
        noise_img = sp_noise(img,0.02)

        imgName = os.path.basename(image)
        imgName = imgName.replace(".jpg","")
        # im.save("flipped/" + imgName + "_flipped.jpg")

        cv2.imwrite('merged/' + imgName + "_noise_" + str(i) +'.jpg', noise_img)