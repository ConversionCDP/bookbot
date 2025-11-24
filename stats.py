def countWords(filePath):
    with open(filePath) as f:
        fileContents = f.read()
        words = fileContents.split()
        totalWords = len(words)
        return totalWords

def characterCount(filePath):
    with open(filePath) as f:
        fileContents = f.read()
        characters = {}
        for char in fileContents:
            if char.lower() in characters:
                characters[char.lower()] = (characters[char.lower()])+1
            else:
                characters[char.lower()] = 1
        return(characters)
    
def sortList(dictionary):
    numList = []
    for item in dictionary:
        newDict = {}
        newDict["char"] = item
        newDict["value"] = dictionary[item]
        numList.append(newDict) 
    numList.sort(reverse=True, key=pullNum)
    return numList

def pullNum(numList):
    return numList['value']

