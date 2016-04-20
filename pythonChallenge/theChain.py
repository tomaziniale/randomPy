# Level 4
# follow the chain
# urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# and the next nothing is 44827

import urllib.request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
data = b'12345'
next = data
results = []

def filterNothingValue(data):
    return (str(data).split(' ')[-1:][0])

for i in range(0,7):
    with urllib.request.urlopen(url) as f:
        next = f.read().decode("utf-8")
        results.append(next)        
    url += filterNothingValue(next)
                            
for line in results: print(line + "\n")

print ("end")

#still in dev...