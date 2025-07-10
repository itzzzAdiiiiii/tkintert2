import cv2

image = cv2.imread('pika.png')
start_point = (0,0)
radius = 7
color = (0,255,0)
thickness = 9

image = cv2.circle(image,start_point,radius,color,thickness)

cv2.imshow("Image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread('pika.png')
start_point = (0,0)
end_point= (250,250)
color = (0,255,0)
thickness = 9

image = cv2.rect(image,start_point,end_point,color,thickness)

cv2.imshow("Image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread('pika.png')
start_point = (0,0)
end_point = (250,250)
color = (0,255,0)
thickness = 9

image = cv2.line(image,start_point,end_point,color,thickness)

cv2.imshow("Image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()
