from stats import countWords, characterCount, sortList

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        print(file_contents)

def main():
    #get_book_text("books/frankenstein.txt")
    totalWords = countWords("books/frankenstein.txt")
    characters = characterCount("books/frankenstein.txt")
    numList = sortList(characters)
    first = (f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {totalWords} total words\n--------- Character Count -------\n")
    charList = []
    for item in numList:
        check = item['char']
        if check.isalpha():
            charList.append(f"{check}: {item['value']}")
    second = "\n".join(charList)
    third = "============= END ==============="
    print(first+second+"\n"+third)

main()