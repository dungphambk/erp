from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

xml = pytesseract.image_to_alto_xml(Image.open(r'F:\Downloads\ERP\erp\erp\addons\sale\models\test.png'))
print(xml)