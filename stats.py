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
    
    #take the values out of the dictionary and sort them in a separate list. Then we need to create a tuple where we take the sorted value and search through the original dictionary for the value to pull the letter. Then put the letter and value in the output from the tupled list. Big Brain
    print(dictSort)

characterCount("books/frankenstein.txt")

