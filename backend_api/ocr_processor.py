import pytesseract
from PIL import Image
import cv2
import numpy as np

# Windows path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

class AmharicOCR:

    @staticmethod
    def preprocess_image(image_path):

        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        thresh = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        return thresh

    @staticmethod
    def extract_text(image_path):

        processed = AmharicOCR.preprocess_image(image_path)

        text = pytesseract.image_to_string(
            processed,
            lang='amh'
        )

        return text