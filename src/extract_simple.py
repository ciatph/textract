import os
from dotenv import load_dotenv
import cv2 as cv
import pytesseract
import numpy as np

load_dotenv()

# Define tesseraact
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_EXECUTABLE_PATH')

def extractTextSimple(img):
  ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
  kernel = np.ones((2,2), np.uint8)
  # img = cv.dilate(thresh, kernel, iterations=1)

  text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
  print(text)
