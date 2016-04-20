#equality
#One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
#http://www.pythonchallenge.com/pc/def/equality.html

text = open('pythonChallenge/equality.txt','r').read()
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

#eq 2
part = [""] * 9
for c in text:    
    del part[0]
    part.append(c)
    if not part[0].isupper() and \
        part[1].isupper() and \
        part[2].isupper() and \
        part[3].isupper() and \
        not part[4].isupper() and \
        part[5].isupper() and \
        part[6].isupper() and \
        part[7].isupper() and \
        not part[8].isupper():
            print (part[4])
            
print ('end 2')