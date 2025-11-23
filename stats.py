def countWords(filePath):
    with open(filePath) as f:
        fileContents = f.read()
        words = fileContents.split()
        totalWords = len(words)
        print(f"Found {totalWords} total words")

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
    dictSort = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    '''for item in dictSort:
        if str(item).isalpha() == False:
            remove dictSort[item]'''
    print(dictSort)

characterCount("books/frankenstein.txt")

