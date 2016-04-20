#equality
#One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
#http://www.pythonchallenge.com/pc/def/equality.html

text = open('equality.txt','r').read()
#text = "SsYjzTfACZPVMAyHWLwDTLsNUfzmzZLPNFmNoVHm"

up = []
dw = []
for i in range(65, 91):
    up.append(chr(i))
for i in range(97, 123):
    dw.append(chr(i))

lenTxt = len(text)

for i,c in enumerate(text):
    if c in dw:
        hit =0;
        if i<lenTxt-1 and text[i+1] in up: hit +=1
        if i<lenTxt-2 and text[i+2] in up: hit +=1
        if i<lenTxt-3 and text[i+3] in up: hit +=1
        if i<lenTxt-4 and text[i+4] in dw: hit +=1
        
        if i>0 and text[i-1] in up: hit +=1
        if i>1 and text[i-2] in up: hit +=1
        if i>2 and text[i-3] in up: hit +=1
        if i>3 and text[i-4] in dw: hit +=1
     
        if hit == 8: print(c)

print('end')