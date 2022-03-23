from tkinter import N


posWords = []
blcLt = []
yelLt = []
grnLt = []
positions = []
allWords = []
with open('sgb-words.txt') as w:
  allWords = w.readlines()

while (len(allWords)>=3):
    del posWords[:]
    del yelLt[:]
    del grnLt[:]
    del positions[:]
    # print(len(allWords))

    blcLt = list(input("New Black Letters:(That are not Yellow or Green) (If none input \"-\") ").replace(" ",""))
    if (blcLt[0]!='-'):
        for letter in blcLt:
            for word in allWords:
                if letter not in word:
                    posWords.append(word)                
            allWords = posWords.copy()
            del posWords[:]
        # print(len(allWords))

    yelLt = list(input("Yellow Letters:(Include the old as position might change) (If none input \"-\") ").replace(" ",""))
    if (yelLt[0]!='-'):
        for letter in yelLt:
            for word in allWords:
                if letter in word:
                    posWords.append(word)
            allWords = posWords.copy()
            del posWords[:]
        # print(len(allWords))

    temp = len(yelLt)
    if (temp != 0 and yelLt[0]!="-"):
        for i in range(temp):
            print("Type the position of the Letter "+ yelLt[i])
            tempPos = int(input("Enter Position:(1-5) "))
            positions.append(tempPos-1)
    
    temp = 0
    for pos in positions:
        for word in allWords:
            # print(len(posWords))
            if word[pos] == yelLt[temp]:
                allWords.remove(word)
        temp+=1

    del positions[:]
    grnLt = list(input("Green Letters:(Include the old ones too) (If none input \"-\") ").replace(" ",""))
    temp = len(grnLt)
    if (temp != 0 and grnLt[0]!="-"):
        for i in range(temp):
            print("Type the position of the Letter "+ grnLt[i])
            tempPos = int(input("Enter Position:(1-5) "))
            positions.append(tempPos-1)
    
    temp = 0
    for pos in positions:
        for word in allWords:
            # print(len(posWords))
            if word[pos] == grnLt[temp]:
                posWords.append(word)
        allWords = posWords.copy();
        del posWords[:]
        temp+=1

    print(len(allWords))
    print(*allWords)

allWords = posWords.copy()
