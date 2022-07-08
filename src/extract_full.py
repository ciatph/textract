import os
from dotenv import load_dotenv
import cv2 as cv
import pytesseract
import numpy as np

load_dotenv()

# Define tesseraact
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_EXECUTABLE_PATH')

def extractText(image):
  # Load image, grayscale, and get (inverse) threshold
  gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
  ret, thresh = cv.threshold(gray, 114, 236, cv.THRESH_BINARY_INV)
  # ret, thresh2 = cv2.threshold(gray, 114, 236, cv2.THRESH_BINARY)

  # Remove horizontal lines
  horizontal_kernel = cv.getStructuringElement(cv.MORPH_RECT, (20,1))
  detect_horizontal = cv.morphologyEx(thresh, cv.MORPH_OPEN, horizontal_kernel, iterations=2)
  cnts = cv.findContours(detect_horizontal, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]
  for c in cnts:
      cv.drawContours(thresh, [c], -1, (255,255,255), 2)

  # Dilate to connect text and remove dots
  kernel = cv.getStructuringElement(cv.MORPH_RECT, (10,10))
  dilate = cv.dilate(thresh, kernel, iterations=2)
  cnts = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]

  for c in cnts:
      area = cv.contourArea(c)
      if area < 500:
          cv.drawContours(dilate, [c], -1, (255,255,255), -1)

  # Bitwise-and to reconstruct image
  result = cv.bitwise_and(image, image, mask=dilate)
  result[dilate==0] = (255,255,255)

  # OCR
  # data = pytesseract.image_to_string(result, lang='eng', config='--psm 6')
  data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
  print(data)

  # Test: Erode image
  # ker = np.ones((3,3), np.uint8)
  # thresh2 = cv.dilate(thresh2, ker, cv.BORDER_REFLECT)

  cv.imshow('thresh', thresh)
  cv.imshow('mask', result)
  cv.imshow('dilate', dilate)
  cv.imwrite('black_n_white.jpg', thresh)
  cv.waitKey()
