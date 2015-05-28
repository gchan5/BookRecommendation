def readBooks(bfilename):
       ''' Read book titles from the file bfilename,
       append each book title to the list books and return it'''
       # FILL IN CODE
       booksf = open(bfilename, "r")
       books = list(booksf)
       for i in range(0, len(books)):
              if "\n" in books[i]:
                   books[i] = books[i].replace("\n", "")
                   
       return books



def readUserProfile(filename) :
       ''' Reads a file with the user profile. The file contains
       the name of the user on the first line and ratings for all the books
       on the next line, separated by white space'''
       # FILL IN CODE
       prof = open(filename, "r")
       profile = list(prof)
       del(profile[0])
       profile = profile[0].split(" ")
       del(profile[len(profile)-1])
       for i in range(0, len(profile)):
              profile[i] = int(profile[i])

       return profile


  
def readRatings(filename):
       ''' Reads the ratings data from the filename and returns a dictionary,
       where each username is the key, and the value is a list of ratings for all the books'''
       dictRatings = {}
       uratings = open(filename, "r")
       lines = list(uratings)
       for i in range(0, len(lines)):
             lines[i] = lines[i].replace("\n", "")
       
       for i in range(0, len(lines), 2):
              lines[i+1] = lines[i+1].split(" ")
              del(lines[i+1][len(lines[i+1])-1])
              for j in range(0, len(lines[i+1])):
                     lines[i+1][j] = int(lines[i+1][j])
              dictRatings[lines[i]] = lines[i+1]

       
       return dictRatings

       
def recommendBooks(books, dictRatings, profile) :
       ''' Takes the list of books,  the dictionary of ratings,
       and the list of ratings for the user, and returns a list of
       recommended books'''
       # FILL IN CODE
       similarityList = []
       recomBooks = []
       
       dkeys = list(dictRatings.keys())
       for names in dkeys:
              sim = 0
              li = []
              for i in range(0, 55):
                     d = dictRatings[names]
                     sim = sim + (profile[i]*d[i])
              li.append(sim)
              li.append(names)
              similarityList.append(li)

       l = similarityList
       sortedL = sorted(l, reverse = True)

       mosts = sortedL[0:6]
       
       for i in range(0,5):
              name = mosts[i][1]
              dlist = dictRatings[name]
              b = 0
              for j in range(0, 55):
                     if dlist[j] == 5 and profile[j] == 0:
                            if books[j] not in recomBooks:
                                   recomBooks.append(books[j])
                                   b += 1
                                   if b > 4:
                                          break


                                   
       print(recomBooks)
       return recomBooks
                           
       
       
                      
       

def writeBooksToFile(recomBooks, filename):
       ''' Write the list of recommended books to a file'''
       file = open(filename, "w")
       for i in range(0, len(recomBooks)):
              file.write(recomBooks[i] + "\n")
       

       file.close()

  
def main() :
       # First, read the books, save the return value to the list books
       # Then, read the user's profile file
       # Then, read the ratings
       # Call recommendBooks to get a list of recommended books
       # Write this list to file "recommendedBooks.txt"

       # FILL IN CODE'''
       books = readBooks("books.txt")
       profile = readUserProfile("profile.txt")
       dictRatings = readRatings("ratings.txt")
       recomBooks = recommendBooks(books, dictRatings, profile)
       writeBooksToFile(recomBooks, "recommendedBooks.txt")



#main()
