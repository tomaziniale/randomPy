# OCR
# http://www.pythonchallenge.com/pc/def/ocr.html
text = open('texto.txt', 'r').read()
o = {}

for c in text:
    if c in o:
        continue
    o[c] = text.count(c)
    if o[c] < 10:
        print(c)

print(o)
