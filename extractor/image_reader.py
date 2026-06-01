import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_image(path):
    print("\n===================================")
    print("         OCR PROCESSING")
    print("===================================\n")
    print("Reading Image :", path)
    
    
    img = Image.open(path)

    text = pytesseract.image_to_string(img)
    print("\nEXTRACTED TEXT:\n")
    print(text[:250])

    return text

