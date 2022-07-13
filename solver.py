import cv2
import pytesseract
config = ('-l eng --oem 1 --psm 3')
import numpy as np
img = cv2.imread("samplecaptcha/2.jpeg")
lower_white = (180,180,180)
higher_white = (255,255,255)
white_range = cv2.inRange(img, lower_white, higher_white)
cv2.imshow("image", white_range)
text = pytesseract.image_to_string(white_range, config=config)
print(text)
cv2.waitKey(3000)

cv2.destroyAllWindows()
