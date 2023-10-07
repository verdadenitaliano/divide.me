from pdf2image import convert_from_path
import pytesseract
import utility
from skimage.filters import threshold_local
from PIL import Image

from ReceiptParser import ReceiptParser


POPPLER_PATH = r'C:\poppler-23.08.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Sample file out of the dataset
# file_name = '../resources/fu2.jpeg'
# img = Image.open(file_name)
# img.thumbnail((800, 800), Image.LANCZOS)


def extract(file_path, file_format):
    # extract text from img file using utility.py
    extract_doc = utility.preprocess_image(file_path)
    #text = pytesseract.image_to_string(img, lang='eng')
    #document_text = '\n' + text

    if file_format == 'receipt':
        extracted_data = ReceiptParser(extract_doc).parse()
    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data

    #extracting from img file
    #if file_format =='receipt':
     #   pass #extract data from invoice
    #elif file_format == 'patient_details':
     #   pass #extract data from patient form

if __name__ == '__main__':
    data = extract('../resources/lavaniya_4.jpeg', 'receipt')
    print(data)