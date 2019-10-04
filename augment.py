import cv2
import sys
import os
import glob
from PIL import Image
from PIL import ImageOps

imageDirectory = sys.argv[1]
print(imageDirectory)
images = os.listdir(imageDirectory)
print(len(images))

img_path = glob.glob(imageDirectory + '/*.jpg')
print(img_path[1])
for image in img_path:
    im = Image.open(image)
    im = ImageOps.mirror(im)
    imgName = os.path.basename(image)
    imgName = imgName.replace(".jpg","")
    im.save("flipped/" + imgName + "_flipped.jpg")


'''
in_dir = '../Concerned'
save_img_dir = '../images'
img_paths = glob.glob(in_dir + '/*.jpg' )

print(img_paths)

for imagePath in img_paths:
    imageName = (os.path.split(imagePath)[-1])
    imageName = imageName.replace(".jpg","")
    
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=2.0,
        minNeighbors=4,
        minSize=(40, 40)
    )

    print("[INFO] Found {0} Faces.".format(len(faces)))
    i = 0
    for (x, y, w, h) in faces:  
        i = i + 1
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)
        roi_color = image[y:y + h, x:x + w]
        print("[INFO] Object found. Saving locally.")
        cv2.imwrite(os.path.join(save_img_dir,(str(i) + '_' + str(imageName))) + '_faces.jpg', roi_color)

# status = cv2.imwrite('faces_detected.jpg', image)
# print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
'''