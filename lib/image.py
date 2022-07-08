import cv2 as cv
import numpy as np

# A set of wrapper functions for OpenCV's image object

def showImage(windowName, img, write = False):
  '''
  Displays the loaded image file. Press any key to dismiss the window.
    Parameters:
      windowName (string): Window title.
      img (OpenCV Image): Image file loaded by opencv
      write (bool): true|false write the picture file to <windowName>.jpg
  '''
  cv.imshow(windowName, img)
  if write:
    writeImage(windowName, img)
  cv.waitKey(0)

def writeImage(filename, img):
  '''
  Write an image to file.
    Parameters:
      filename (string): Full path to a target image file.
      img: (OpenCV Image) Image object
  '''
  cv.imwrite(filename, img)

def loadImage(path):
  '''
  Loads an RGBimage file with its default colors.
    Parameters:
      path (string): Full path to an image file.
    Returns:
      img (OpenCV Image): Image object
  '''
  return cv.imread(path)

def loadGrayscale(path):
  '''
  Loads an image file in grayscale.
    Parameters:
      path (string): Full path to an image file.
    Returns:
      img (OpenCV Image): Image object
  '''
  return cv.imread(path, 0)

def grayScale(img):
  '''
  Turn an image to grayscale.
    Parameters:
      img (OpenCV Image): Image object
    Returns:
      img (OpenCV Image): Image in gray scale
  '''
  return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def crop(img, y, x, height, width):
  '''
  Crops a part of an image.
  Parameters:
    img (OpenCV Image): Image object
    y (int): target y-coordinate on the img to start cropping
    x (int): target x-coordinate on the img to start cropping
    height (int): Height of image to crop
    width (int): Width of image to crop
  Returns:
    img (OpenCV Image): Cropped image
  '''
  return img[y:y+height, x:x+width]

def scaleImage(img, scale):
  '''
  Scales an image according to the scale factor.
  Parameters:
    img (OpenCV Image): Image object
    scale (int): Scaling factor
  Returns:
    img (OpenCV Image): Scaled image
  '''
  return cv.resize(img, None, fx=scale, fy=scale)

def binarizeImage(image, lower = [114, 114, 114], upper = [255, 255, 255]):
  '''
  Creates a binarized (1, 0) version of an RGB or gray scale image.
  Parameters:
    img (OpenCV Image): RGB or grayscale image object
    lower (int array): RGB of the lower color threshold
    upper (int array): RGB of the upper color threshold
  Returns:
    img (OpenCV Image): Binarized image
  '''
  isColored = (len(image.shape) == 3)

  if isColored:
    img = grayScale(image)
  else:
    img = image

  img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

  gray_lower = np.array(lower)
  gray_upper = np.array(upper)

  return cv.inRange(img, gray_lower, gray_upper)

