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

                
            if i>=2:
                item1=theMatrix[i-2][j-1]*gramBank2[word[i-2:i]]
            else:
                item1=float('inf')
            if i>=3:
                item2=theMatrix[i-3][j-1]*gramBank3[word[i-3:i]]
            else:
                item2=float('inf')
            if i>=4:
                item3=theMatrix[i-4][j-1]*gramBank4[word[i-4:i]]
            else:
                item3=float('inf')
            if i>=5:
                item4=theMatrix[i-4][j-1]*gramBank5[word[i-5:i]]
            else:
                item4=float('inf')
            tem.append(min(item1,item2,item3,item4))
            ##print (min(item1,item2,item3,item4))
            j=j+1
        theMatrix.append(tem)
        i=i+1
    ##for item in theMatrix:
 ##       print (item)
    resultList=[]
    for score in theMatrix[-1]:
        score=(float(score))**(3/(len(word)))
        resultList.append(score)
    return min(resultList)
        
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
##print (scoreByRanking('vitualbox'))
fw1.close()
fw2.close()
fr1.close()
fr2.close()
##print (gramBank2)
##print (gramBank3)
##print (gramBank4)
##print (gramBank5)




