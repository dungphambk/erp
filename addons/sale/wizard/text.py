from PIL import Image
import pytesseract
text = pytesseract.image_to_string(Image.open(r'/Users/William/Downloads/Odoo16/erp/print_sample.png'))
text_after_split = text.split('\n')
text_after_split = list(filter(None, text_after_split))
order_date = ''
customer = ''
print(text_after_split)
for i in range(len(text_after_split)):
	if ('Order Date' in text_after_split[i]): order_date =text_after_split[i][12:]
	if ('Address' in text_after_split[i]): customer = text_after_split[i+1]
customer = customer.split(',')[0]