import string
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def analyzeText(text):
    LEXICON_PATH = './NRC-Emotion-Lexicon-Wordlevel-v0.92.txt'
    lexicon = readFile(LEXICON_PATH)
    lexiconDict = createLexiconDict(lexicon)
    emotionCounts = {}
    numWords = 0
    for word in text.split():
        numWords += 1
        stripped = word.translate(str.maketrans('', '', string.punctuation)).lower()
        if stripped in lexiconDict.keys():
            print(stripped, lexiconDict[stripped])
            for emotion in lexiconDict[stripped]:
                if emotion not in emotionCounts.keys():
                    emotionCounts[emotion] = 0
                else:
                    emotionCounts[emotion] += 1
        
    return emotionCounts, numWords

def createLexiconDict(lexicon): #o(n) runtime
    lexiconDict = {}
    for line in lexicon.splitlines():
        words = line.split('\t')
        if words [2] == '0':
            continue
        if words[0] not in lexiconDict.keys():
            lexiconDict[words[0]] = []
        lexiconDict[words[0]].append(words[1])
    return lexiconDict
            

# print(analyzeText(SAMPLE_POEM, lexicon))
# print(createLexiconDict(lexicon))
# createLexiconDict(lexicon)
# print(lexicon)
# print('worn    anticipation    0'.split(' '))
# print('yearning        anticipation    1'.split(' '))
