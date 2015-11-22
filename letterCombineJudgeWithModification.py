##def letterCombineJudge(word):
gramBank2={}
gramBank3={}
gramBank4={}
gramBank5={}


def scoreByRanking(word):
    word=word.strip()
    word=word.lower()
    maxTime=(len(word))/2
    maxLength=len(word)
    if maxLength<=1:
        return 1
    theMatrix=[]
    backward=[]
    i=0
    tem=[]
    while i<maxTime:
        tem.append(1)
        i=i+1
    theMatrix.append(tem)
    i=0
    tem=[]
    while i<maxTime:
        tem.append(float('inf'))
        i=i+1
    theMatrix.append(tem)
    i=2
    while i<=maxLength:
        j=0
        tem=[]
        temBack=[]
        while j<maxTime:
            if j<i/5:
                tem.append(float('inf'))
                temBack.append(float('inf'))
                j=j+1
                continue
            
            if word[i-2:i] in gramBank2.keys():
                k=1
            else:
                gramBank2[word[i-2:i]]=float('inf')
            if word[i-3:i] in gramBank3.keys():
                k=1
            else:
                gramBank3[word[i-3:i]]=float('inf')
            if word[i-4:i] in gramBank4.keys():
                k=1
            else:
                gramBank4[word[i-4:i]]=float('inf')
            if word[i-5:i] in gramBank5.keys():
                k=1
            else:
                gramBank5[word[i-5:i]]=float('inf')

            item=[]
            second=[]
            if i>=2:
                item.append(theMatrix[i-2][j-1]*gramBank2[word[i-2:i]])
            else:
                item.append(float('inf'))
            if i>=3:
                item.append(theMatrix[i-3][j-1]*gramBank3[word[i-3:i]])
            else:
                item.append(float('inf'))
            if i>=4:
                item.append(theMatrix[i-4][j-1]*gramBank4[word[i-4:i]])
            else:
                item.append(float('inf'))
            if i>=5:
                item.append(theMatrix[i-5][j-1]*gramBank5[word[i-5:i]])
            else:
                item.append(float('inf'))
            choice=min(item)
            indexChoice=item.index(choice)
            temBack.append([i-2-indexChoice,j-1])
            tem.append(choice)
            ##print (min(item1,item2,item3,item4))
            j=j+1
        theMatrix.append(tem)
        backward.append(temBack)
        i=i+1
    ##print (backward)
    segment=[]
    times=theMatrix[-1].index(min(theMatrix[-1]))
    length=len(word)
    while times>0:
        print (length,times)
        last=backward[length-2][times]
        segment.append(word[last[0]:length])
        length=last[0]
        times=last[1]
    segment.reverse()
    print (segment)

    eachscore=[]
    chengji=1
    for seg in segment:
        if len(seg)==2:
            eachscore.append(gramBank2[seg])
        if len(seg)==3:
            eachscore.append(gramBank3[seg])
        if len(seg)==4:
            eachscore.append(gramBank4[seg])
        if len(seg)==5:
            eachscore.append(gramBank5[seg])
        chengji=chengji*eachscore[-1]
    print (chengji,min(theMatrix[-1]))

    if min(theMatrix[-1])==float('inf'):
        finalScore=float('inf')
    else:
        minEachScore=min(eachscore)
        minIndex=eachscore.index(minEachScore)
        eachscore.pop(minIndex)
        finalScore=min(theMatrix[-1])/(minEachScore*min(eachscore))
##        maxEachScore=max(eachscore)
##        maxIndex=eachscore.index(maxEachScore)
##        eachscore.pop(maxIndex)
##        finalScore=max(eachscore)*maxEachScore
    return finalScore
    ##for item in theMatrix:
 ##       print (item)
##    resultList=[]
##    for score in theMatrix[-1]:
##        score=(float(score))**(3/(len(word)))
##        resultList.append(score)
##    return min(resultList)
        
def loadDic():
    fw2=open('rankingList2.txt','r')
    fw3=open('rankingList3.txt','r')
    fw4=open('rankingList4.txt','r')
    fw5=open('rankingList5.txt','r')

    rankList=fw2.readlines()
    for line in rankList:
        gramBank2[(line.split(' '))[0]]=int((line.split(' '))[1])
    rankList=fw3.readlines()
    for line in rankList:
        gramBank3[(line.split(' '))[0]]=int((line.split(' '))[1])
    rankList=fw4.readlines()
    for line in rankList:
        gramBank4[(line.split(' '))[0]]=int((line.split(' '))[1])
    rankList=fw5.readlines()
    for line in rankList:
        gramBank5[(line.split(' '))[0]]=int((line.split(' '))[1])
    fw2.close()
    fw3.close()
    fw4.close()
    fw5.close()
    
loadDic()
fr1=open('wordbank.txt','r')
fr2=open('wrongword.txt','r')
fw1=open('wordscores.txt','w')
fw2=open('wrongwordscores.txt','w')
score1={}
score2={}
allWords=fr1.readlines()
for word in allWords:
    word=word.strip()
    word=word.lower()
    if(len(word)==9):
        print (word,' 1')
        score1[word]=scoreByRanking(word)

allWords=fr2.readlines()
for word in allWords:
    word=word.strip()
    word=word.lower()
    if(len(word)==9):
        print (word,' 2')
        score2[word]=scoreByRanking(word)
    
listtest= sorted(score1.items(), key=lambda score1:score1[1])
for letters in listtest:
    fw1.write(str(letters)+'\n')
listtest= sorted(score2.items(), key=lambda score2:score2[1])
for letters in listtest:
    fw2.write(str(letters)+'\n')
print (scoreByRanking('vitualbox'))
fw1.close()
fw2.close()
fr1.close()
fr2.close()
##print (gramBank2)
##print (gramBank3)
##print (gramBank4)
##print (gramBank5)




