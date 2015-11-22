import sys


def number(iteration):
    if(iteration<=9):
        return '0000'+str(iteration)
    elif(iteration<=99):
        return '000'+str(iteration)
    elif(iteration<=999):
        return '00'+str(iteration)
    elif(iteration<=9999):
        return '0'+str(iteration)
    else:
        return str(iteration)

iteration=1
wordList=[]
while 1>0:
    try:
        count=number(iteration)
        route='TEST'+'.'+count+'.txt'
        fr=open(route,'r')
        allWord=fr.readlines()
        fr.close()
        for line in allWord:
            temlist=line.split(' ')
            for word in temlist:
                word=word.strip()
                if word.isalpha():
                    wordList.append(word.lower())
        iteration=iteration+1
    except:
        iteration=iteration+1
    if iteration==30000:
        break
fw=open('wordbank.txt','w')
for word in wordList:
    fw.write(word+'\n')
fw.close()
