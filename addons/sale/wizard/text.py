from PIL import Image
import re
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'  # Win

text = pytesseract.image_to_string(Image.open(
    r'F:/Downloads/ERP/erp/erp/print_sample.png'))
text_after_split = list(filter(None, text.split('\n')))

order_date = ''
customer = ''
productsIndex = 0
quantityIndex = 0
unitPriceIndex = 0
taxesIndex = 0

for i in range(len(text_after_split)):
    if ('Order Date' in text_after_split[i]):
        order_date = text_after_split[i][12:]
    if ('Address' in text_after_split[i]): customer = text_after_split[i+1]
    if ('Products' in text_after_split[i]):
        productsIndex = i
    if ('Quantity' in text_after_split[i]): quantityIndex = i
    if ('Unit Price' in text_after_split[i]):
        unitPriceIndex = i
    if ('Tax' in text_after_split[i]): taxesIndex = i

customer = customer.split(',')[0]

product = []
for i in text_after_split[productsIndex+1:quantityIndex]:
    m = re.search('\[(.+?)\]', i)
    if m:
        product.append(m.group(1))
print(customer)
print(product)

quantity = []
for i in text_after_split[quantityIndex+1:unitPriceIndex]:
    quantity.append(i.split(' ')[0])
print(quantity)

unitPrice = []
for i in text_after_split[unitPriceIndex+1:taxesIndex]:
    unitPrice.append(i.split(' ')[0])
print(unitPrice)
