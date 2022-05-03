import os
import cv2
from PIL import Image
import numpy

def func(dataDir, output):
    array = []
    for file in os.listdir(dataDir):
        filePath = os.path.join(dataDir, file)
        image = Image.open(filePath)
        newImage = image.resize((28, 28))
        greyscaleImage = newImage.convert('L')
        greyscaleImage.save('newImage.png')

        img_array = cv2.imread('newImage.png')
        x = []
        for i in range(28):
            for j in range(28):
                x.append(img_array[i][j][0])

        #img_data = img_array.reshape(784)
        x = numpy.array(x)
        img_data = (x / 255.0 * 0.99) + 0.01
        array.append(img_data)


    a_file = open(output, "w")
    for row in array:
        numpy.savetxt(a_file, row)

    a_file.close()


path = "C:/Users/shahs/OneDrive/Desktop/New folder (2)"
for i in os.listdir(path):
    func(os.path.join(path, i), os.path.join(path, f'{i}.txt'))
    print(i)