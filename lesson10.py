import cv2

img = 'cat.jpg'
cat_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
image_read = cv2.imread(img)
cat_face = cat_face_cascade.detectMultiScale(image_read)
cat = Image.open(img)
glasses = Image.open('glasses.jpg')

for (x, y, w, h) in cat_face:
    cv2.rectangle(image_read, (x, y), (x+w, y+h), (0, 0, 255), 3)
    cv2.imshow('cat', image_read)
    cv2.waitKey()
