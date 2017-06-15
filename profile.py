def readBooks(booksFilename):
    booksf = open(booksFilename, "r")
    books = list(booksf)
    for i in range(0, len(books)):
        if "\n" in books[i]:
            books[i] = books[i].replace("\n", "")
    return books

print(readBooks("books.txt"))

def enterUserProfile(books, filename):
    profile = open(filename, "w")
    name = input("Please enter your username: ")
    profile.write(name + "\n")
    print("Please create your profile by rating the following books from -5 to 5: ")
    for i in books:
       print(i)
       rating = input("Enter your rating: ")
       profile.write(rating)
       profile.write(" ")

    profile.close()

def main():
    bookList = readBooks("books.txt")
    enterUserProfile(bookList, "profile.txt")

main()
    
    
