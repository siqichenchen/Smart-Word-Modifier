import sys
import os
import random
fr=open('wordbank.txt','r')
fw=open('wrongword.txt','w')
whole=fr.readlines()
for word in whole:
    word=word.strip()
    word=word.lower()
    if len(word)==1:
        fw.write(word+'\n')
        continue
    way=random.randint(0, 2)
    if way==0:
        digit=random.randint(0, len(word)-1)
        newWord=word[0:digit]+word[digit+1:]
    elif way==1:
        digit=random.randint(0, len(word)-1)
        letter=random.randint(97, 122)
        newWord=word[0:digit]+chr(letter)+word[digit:]
    else:
        first=random.randint(0, len(word)-2)
        second=random.randint(first,len(word)-1)
        newWord=word[:first]+word[second:second+1]+word[first+1:second]+word[first:first+1]+word[second+1:]
    fw.write(newWord+'\n')

fr.close()
fw.close()
