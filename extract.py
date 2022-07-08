import json
from lib.image import *
from src.groups import showGroups
from src.extract_simple import extractTextSimple

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

  # Write grayscale image to file
  writeImage('gray.jpg', img)

  # Load the grayscale image from file
  gray = loadGrayscale('gray.jpg')
  gray = scaleImage(gray, 4)
  gray = binarizeImage(gray)
  extractTextSimple(gray)

  showGroups(img)

if __name__ == '__main__':
  main()
