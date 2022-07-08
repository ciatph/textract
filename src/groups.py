import cv2 as cv
import pytesseract
import numpy as np

# Define tesseraact
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def showGroups(mask):
  img_contour = mask
  img = mask

  ret, thresh_value = cv.threshold(img_contour, 114, 236, cv.THRESH_BINARY_INV)
  # thresh_value = cv.threshold(img, 94, 236, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]

  kernel = np.ones((10,10), np.uint8)
  dilated_val = cv.dilate(thresh_value, kernel, iterations=1)

  contours, hierarchy = cv.findContours(
    dilated_val, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

  for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    if y < 450: # 90
      img = cv.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 1)

  cv.imshow('groups', img)
  cv.waitKey(0)
