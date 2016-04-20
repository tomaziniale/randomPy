# Level 1
# http://www.pythonchallenge.com/pc/def/map.html
# everybody thinks twice before solving this.
# What about making trans?

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
    amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
    ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
    lmu ynnjw ml rfc spj."""
    
#intab = "abcdefghijklmnopqrstuvwxyz"
#outtab= "cdefghijklmnopqrstuvwxyzab"
intab = ""
outtab = ""
for i in range(97, 123): intab += chr(i)
for i in range(99, 123): outtab += chr(i)
outtab += "ab"

print(text.translate({ord(x): y for (x, y) in zip(intab, outtab)})) 