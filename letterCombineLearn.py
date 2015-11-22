import sys
import os

readfile="wordbank.txt"
writefile2="2gramCombineBank.txt"
writefile3="3gramCombineBank.txt"
writefile4="4gramCombineBank.txt"
writefile5="5gramCombineBank.txt"
frequency2={}
frequency3={}
frequency4={}
frequency5={}
fr=open(readfile,'r')
fw2=open(writefile2,'w')
fw3=open(writefile3,'w')
fw4=open(writefile4,'w')
fw5=open(writefile5,'w')
wordlist=fr.readlines()
for word in wordlist:
    word=word.strip()

    first=0
    last=first+2
    while last<=len(word):
        tem=word[first:last].lower()
        if tem in frequency2.keys():
            frequency2[tem]=frequency2[tem]+1
        else:
            frequency2[tem]=1
        
        first=first+1
        last=last+1
        
    first=0
    last=first+3
    while last<=len(word):
        tem=word[first:last].lower()
        if tem in frequency3.keys():
            frequency3[tem]=frequency3[tem]+1
        else:
            frequency3[tem]=1
        
        first=first+1
        last=last+1
        
    first=0
    last=first+4
    while last<=len(word):
        tem=word[first:last].lower()
        if tem in frequency4.keys():
            frequency4[tem]=frequency4[tem]+1
        else:
            frequency4[tem]=1
        
        first=first+1
        last=last+1
    first=0
    last=first+5
    while last<=len(word):
        tem=word[first:last].lower()
        if tem in frequency5.keys():
            frequency5[tem]=frequency5[tem]+1
        else:
            frequency5[tem]=1
        
        first=first+1
        last=last+1

for letters in frequency2.keys():
    fw2.write(letters+' '+str(frequency2[letters])+'\n')
for letters in frequency3.keys():
    fw3.write(letters+' '+str(frequency3[letters])+'\n')
for letters in frequency4.keys():
    fw4.write(letters+' '+str(frequency4[letters])+'\n')
for letters in frequency5.keys():
    fw5.write(letters+' '+str(frequency5[letters])+'\n')
    
fr.close()
fw2.close()
fw3.close()
fw4.close()
fw5.close()
fw=open('2gramsorted.txt','w')
listtest= sorted(frequency2.items(), key=lambda frequency2:frequency2[1])
for letters in listtest:
    fw.write(str(letters)+'\n')
fw.close()
fw=open('3gramsorted.txt','w')
listtest= sorted(frequency3.items(), key=lambda frequency3:frequency3[1])
for letters in listtest:
    fw.write(str(letters)+'\n')
fw.close()
fw=open('4gramsorted.txt','w')
listtest= sorted(frequency4.items(), key=lambda frequency4:frequency4[1])
for letters in listtest:
    fw.write(str(letters)+'\n')
fw.close()
fw=open('5gramsorted.txt','w')
listtest= sorted(frequency5.items(), key=lambda frequency5:frequency5[1])
for letters in listtest:
    fw.write(str(letters)+'\n')
fw.close()

gramBank2=[]
gramBank3=[]
gramBank4=[]
gramBank5=[]
fw2=open('2gramsorted.txt','r')
fw3=open('3gramsorted.txt','r')
fw4=open('4gramsorted.txt','r')
fw5=open('5gramsorted.txt','r')
list2=fw2.readlines()
for item in list2:
    word=item[2:4]
    fre=int(item[7:-2])
    gramBank2.append([word,fre])
list3=fw3.readlines()
for item in list3:
    word=item[2:5]
    fre=int(item[8:-2])
    gramBank3.append([word,fre])
list4=fw4.readlines()
for item in list4:
    word=item[2:6]
    fre=int(item[9:-2])
    gramBank4.append([word,fre])
list5=fw5.readlines()
for item in list5:
    word=item[2:7]
    fre=int(item[10:-2])
    gramBank5.append([word,fre])
fw2.close()
fw3.close()
fw4.close()
fw5.close()

gramBank2.reverse()
gramBank3.reverse()
gramBank4.reverse()
gramBank5.reverse()

ranking=1
ties=0
current=gramBank2[0][1]
fw2=open('rankingList2.txt','w')
for eachItem in gramBank2:
    if current==eachItem[1]:
        ties=ties+1
        fw2.write(eachItem[0]+' '+str(ranking)+'\n')
    else:
        current=eachItem[1]
        ranking=ranking+ties
        ties=1
        fw2.write(eachItem[0]+' '+str(ranking)+'\n')
fw2.close()

ranking=1
ties=0
current=gramBank3[0][1]
fw3=open('rankingList3.txt','w')
for eachItem in gramBank3:
    if current==eachItem[1]:
        ties=ties+1
        fw3.write(eachItem[0]+' '+str(ranking)+'\n')
    else:
        current=eachItem[1]
        ranking=ranking+ties
        ties=1
        fw3.write(eachItem[0]+' '+str(ranking)+'\n')
fw3.close()

ranking=1
ties=0
current=gramBank4[0][1]
fw4=open('rankingList4.txt','w')
for eachItem in gramBank4:
    if current==eachItem[1]:
        ties=ties+1
        fw4.write(eachItem[0]+' '+str(ranking)+'\n')
    else:
        current=eachItem[1]
        ranking=ranking+ties
        ties=1
        fw4.write(eachItem[0]+' '+str(ranking)+'\n')
fw4.close()

ranking=1
ties=0
current=gramBank5[0][1]
fw5=open('rankingList5.txt','w')
for eachItem in gramBank5:
    if current==eachItem[1]:
        ties=ties+1
        fw5.write(eachItem[0]+' '+str(ranking)+'\n')
    else:
        current=eachItem[1]
        ranking=ranking+ties
        ties=1
        fw5.write(eachItem[0]+' '+str(ranking)+'\n')
fw5.close()

print (gramBank2)
print (gramBank3)
print (gramBank4)
print (gramBank5)
