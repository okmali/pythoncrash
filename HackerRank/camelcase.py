
import sys
def getWords(combinedWord):
    charsList=list(combinedWord.split(' '))
    words=[]
    for chars in charsList:
        upperpositions=[]
        bracket=[]
        i=0
        for c in list(chars):
            if(c.isupper()):
                upperpositions.append(i)
            elif (c=='('):
                bracket.append(i)    
            i+=1

        beginindex=0
        for index in upperpositions:
            if index==0:
                continue
            words.append(chars[beginindex:index])
            beginindex=index

        if beginindex <len(chars):
            if len(bracket)>0:
                words.append(chars[beginindex:bracket[0]])
            else:    
                words.append(chars[beginindex:])
    retList=[]
    for word in words:
        retList.append(''.join(word))
    return retList

def getFinalWords(words,commands):
    output=''
    wordIndex=0
    for word in words:
        if commands[0].lower()=="s":
                output=output+' '+word.lower()
        elif commands[0].lower()=="c":
            if commands[1].lower()=="c":
                output=output+word.title()
            elif wordIndex==0:    
                output=output+word.lower()
            else:
                output=output+word.title()

        wordIndex+=1

    if commands[0].lower()=="c" and commands[1].lower()=="m":
        output=output+"()"

    return (output.strip())


rawWords=sys.stdin.readlines()
for rawword in rawWords:
    splittedWords=rawword.split(';')
    commands=splittedWords[:2]
    words=getWords(splittedWords[2].strip())
    finalWords=getFinalWords(words,commands)
    print(finalWords)
