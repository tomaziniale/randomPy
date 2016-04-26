# Level 4
# follow the chain
# urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# and the next nothing is 44827

import urllib.request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
data = "12345"
results = []

def filterNothingValue(val):
    return (str(val).split(' ')[-1:][0])

for i in range(0,400):    
    rurl = url + filterNothingValue(data)    
    with urllib.request.urlopen(rurl) as f:
        data = f.read().decode("utf-8")
        results.append(data)
    if "nothing" not in data: 
        print("hint was found at: " + str(i) + ": " + data)
    if "html" in data: break
        
#for line in results: print(line + "\n")

print ("end")