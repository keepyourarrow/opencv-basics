# USAGE
# python index.py --image comic.png
# python index.py --image comic.png --lang de
# python index.py --image comic.png --lang ru

# import the necessary packages
from textblob import TextBlob
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
parser.add_argument("-l", "--lang", type=str, default="es",
	help="language to translate OCR'd text to (default is Spanish)")
args = parser.parse_args()

# load the input image and convert it from BGR to RGB channel
# ordering
image = cv2.imread(args.image)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# use Tesseract to OCR the image, then replace newline characters
# with a single space
text = pytesseract.image_to_string(rgb)
text = text.replace("\n", " ")

# show the original OCR'd text
print("ORIGINAL")
print("========")
print(text)
print("")

# translate the text to a different language
tb = TextBlob(text)
translated = tb.translate(to=args.lang)

# show the translated text
print("TRANSLATED")
print("==========")
print(translated)