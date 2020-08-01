wordfile= open("google-10000-english-no-swears.txt")
wlist = []
#based on frequency of punctuaction based on Meyer (1987)'s analysis of the Brown on http://www.viviancook.uk/Punctuation/PunctFigs.htm which is based on google ngram
symbols = ","*47+"."*45+"--;;():!" 
import random

for i in range(1000):
    line = wordfile.readline()
    word = line.strip()
    if random.randrange(13) == 0:
        word = word.capitalize()
    if random.randrange(5) == 0:
        sybm_num = len(symbols)-1
        word += str(symbols[random.randrange(sybm_num)])
    wlist.append(word)



for i in range(1,11):
    wlist.append(str(i))

for i in range(10):
    wlist.append(str(random.randrange(11,100)))

for i in range(5):
    wlist.append(str(random.randrange(101,1000)))
tenfastfingers_str = "|".join(wlist)

import pyperclip
pyperclip.copy("https://10fastfingers.com/widget/typingtest?dur=600&rand=1&words="+tenfastfingers_str)
print("Done!")

