from stats import countWords, characterCount, sortList

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        print(file_contents)

def main():
    #get_book_text("books/frankenstein.txt")
    countWords("books/frankenstein.txt")
    characters = characterCount("books/frankenstein.txt")
    sortList(characters)

main()