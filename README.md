## textract

Experiments on extracting numerical text as strings from low-resolution graphics.

### Requirements

1. Windows 10
2. Python v3.10.5
3. OpenCV for Python
   - version 4.6.0.66 
   - Installed from `requirements.txt`
4. Tesseract OCR (for Windows)
   - [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) - Installer for Windows
   - [tesseract-ocr-w64-setup-v5.1.0.20220510.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.1.0.20220510.exe)

## Installation

1. Clone this repository.  
`git clone https://github.com/ciatph/textract.git`
2. Install dependencies.  
`pip install -r requirements.txt`
3. Create a `.env` file from the `.env.example` file.
   - Replace the `TESSERACT_EXECUTABLE_PATH` variable with Tesseract's installation path on your machine.

## Usage

1. Run any of the python scripts below on the command line.
2. Press ENTER to clear the image windows.
3. Compare the accuracy of resulting extracted text to the image files.

### Scripts

### `python main.py`

Extracts numerical text using more complete image operations. Shows the `binarized` and `grayscale` versions of the cropped image target, and surrounds significant objects on bounding boxes.

### `python extract.py`

Extracts numerical text from grayscale, binarized image files. Draws bounding boxes on signnificant objects.

@ciatph  
20220708
