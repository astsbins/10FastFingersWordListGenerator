fileA = open("google-10000-english-no-swears.txt")
wlist = []
symbols = ",,,,,,,,,,,,,,,,,,,,,,,,,,,,<................>/???????????;;;;;:::::::[{]]==-_)(*&^%$#@!!!!!!!!!!!!"
import random

for i in range(1000):
    line = fileA.readline()
    w = line.strip()
    if random.randrange(13) == 0:
        w = w.capitalize()
    if random.randrange(5) == 0:
        sybm_num = len(symbols)-1
        w += str(symbols[random.randrange(sybm_num)])
    wlist.append(w)

for i in range(1, 10):
    for i in range(9):
        wlist.append(str(i))

for i in range(100):
    wlist.append(str(i))
worldlist = "|".join(wlist)

import pyperclip
pyperclip.copy("https://10fastfingers.com/widget/typingtest?dur=600&rand=1&words="+worldlist)
# print(worldlist)

