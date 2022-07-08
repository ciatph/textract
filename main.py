import json
from lib.image import *
from src.groups import showGroups
from src.extract_full import extractText

# Data imports
with open('data/coordinates.json', 'r') as f:
  coordinates = json.load(f)

def getRegion(img, region):
  return crop(img,
    coordinates[region]['y'], coordinates[region]['x'],
    coordinates[region]['height'], coordinates[region]['width'])

# Main Program
def main():
  # Load, crop, scale and binarize picture of interest
  img = loadGrayscale('data/regions.JPG')
  img = getRegion(img, 'Region5')
  img = scaleImage(img, 3)
  writeImage('gray.jpg', img)

  img = binarizeImage(img)
  showImage('binarized', img)

  # Load the grayscale image
  grayRGB = loadImage('gray.jpg')
  showImage('grayscale', grayRGB)

  # TO-DO: Process image here
  showGroups(img)
  extractText(grayRGB)

if __name__ == '__main__':
  main()
