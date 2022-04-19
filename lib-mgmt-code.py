class Library_Management:
    
                                           #FUNCTIONS OF THE CODE:
    #OPTION 1
    def login_func(self):
        print("Please fill the following to login: ")
        email = input("Enter your email: ")
        pw = input("Enter your password: ")
        with open("ListOfUsers.txt", "r+") as file:
            file.seek(0)
            data = file.readlines()
            listUser = []
            for user in data:
                user = user.split("-")
                LastItem = user.pop()
                Last = ""
                for char in LastItem:
                    if char == "\n":
                        continue
                    else:
                        Last += char
                user.append(Last)
                listUser.append(user)
            file.close()
        if [email, pw] in listUser:
            print("Login successful.")
            print()
            return [True, email, pw]
        else:
            print("Login unsuccessful.")
            print()
            return [False, email, pw]

    #OPTION 2
    def signup_func(self):
        print("""Welcome to the Sign-Up page
Please fill the following:
""")
        email = input("Enter your email: ")
        pw = input("Enter your password: ")
        with open("ListOfUsers.txt", "r+") as file:
            file.seek(0)
            data = file.readlines()
            listUser = []
            for item in data:
                item = item.split("-")
                LastItem = item.pop()
                Last = ""
                for char in LastItem:
                    if char == "\n":
                        continue
                    else:
                        Last += char
                item.append(Last)
                listUser.append(item)
            file.close()
        for item in listUser:
            if email == item[0]:
                print("A user already exists with the same email, please enter a different one.")
                print()
                return False
            else:
                with open("ListOfUsers.txt", "a+") as file:
                    toAppend = email+"-"+pw
                    file.write("\n")
                    file.write(toAppend)
                    print("New account has been registered.")
                    print()
                return True

    #OPTION 3
    def edit_book_func(self):
        with open("ListOfBooks.txt", "a+") as file:
            file.seek(0)
            data = file.readlines()
            listBook = []
            for book in data:
                book = book.split("-")
                LastItem = book.pop()
                Last = ""
                for char in LastItem:
                    if char == "\n":
                        continue
                    else:
                        Last += char
                book.append(Last)
                listBook.append(book)
            file.close()
        print("The following books are available in the library: ")
        for book in range(len(listBook)):
            print("Book Serial Number: ", book+1)
            print(f" " * 20 + f"{listBook[book][0]}")
            print("Author Of The Book: ")
            print(f" " * 20 + f"{listBook[book][1]}")
            print("Stock Of The Book Available: ")
            print(f" " * 20 + f"{listBook[book][2]}")
            print("Genre Of The Book: ")
            print(f" " * 20 + f"{listBook[book][3]}")
            print("_" * 50)
        print()
        bookNo = int(input("Enter the serial number of the book you want to edit: "))
        bookNo -= 1
        editBook = listBook[bookNo]
        listBook.remove(editBook)
        while True:
            print()
            print("""Select a field you want to edit:
                     1. Title of the book
                     2. Author name of the book
                     3. Stock that is available for the book
                     4. Genre of the book
                     5. Exit
                     """)
            choice = int(input("Enter your choice number: "))
            print()
            if choice == 5:
                break
            if choice == 1:
                bookName = input("Enter new title of the book: ")
                editBook[0] = bookName
                print("The title has been changed.")
            if choice == 2:
                authorName = input("Enter new author name of the book: ")
                editBook[1] = authorName
                print("The author\'s name has been changed.")
            if choice == 3:
                stock = input("Enter new quantity of the book: ")
                editBook[2] = stock
                print("The available number of stock has been changed.")
            if choice == 4:
                genre = input("Enter the genre of the book: ")
                editBook[3] = genre
                print("The genre has been changed.")
        listBook.append(editBook)
        with open("ListOfBooks.txt", "w+") as file:
            for book in listBook:
                if book != listBook[-1]:
                    toWrite = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                    file.write(toWrite + "\n")
                else:
                    toWrite = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                    file.write(toWrite)

    #OPTION 4
    def search_book_func(self):
        bookName = ""
        authorName = ""
        while True:
            print("""Select a field you want to search:
                     1. Title of the book
                     2. Author of the book
                     3. Exit
                     """)
            choice = int(input("Enter your choice number: "))
            if choice == 1:
                bookName = input("Enter book name you want to search: ")
            if choice == 2:
                authorName = input("Enter author name you want to search: ")
            if choice == 3:
                break
        with open("ListOfBooks.txt", "a+") as file:
            file.seek(0)
            data = file.readlines()
            listBook = []
            for book in data:
                book = book.split("-")
                LastItem = book.pop()
                Last = ""
                for char in LastItem:
                    if char == "\n":
                        continue
                    else:
                        Last += char
                book.append(Last)
                listBook.append(book)
            resultsFound = []
            for book in listBook:
                if book[0] == bookName:
                    resultsFound.append(book)
                if book[1] == authorName:
                    resultsFound.append(book)
            return resultsFound

    #OPTION 5
    def display_records_func(self):
        results = self.sort_books_func()
        for book in range(len(results)):
            string1 = "S.NO       BOOK NAME"
            string2 = "QTY        GENRE                     AUTHOR"
            string1 += f"\n{str(book + 1):11}{results[book][0]}"
            string2 += f"\n{results[book][2]:11}{results[book][3]:26}{results[book][1]}"
            final_string = string1 + "\n" + string2
            print(final_string)
            print("-"*100)
        return ''
    def sort_books_func(self):
        with open("ListOfBooks.txt", "a+") as file:
            file.seek(0)
            data = file.readlines()
            listBook = []
            for book in data:
                book = book.split("-")
                LastItem = book.pop()
                Last = ""
                for char in LastItem:
                    if char == "\n":
                        continue
                    else:
                        Last += char
                book.append(Last)
                listBook.append(book)
        length = len(listBook)
        for i in range(length-1):
            for j in range(length-i-1):
                if listBook[j] > listBook[j+1]:
                    listBook[j], listBook[j+1] = listBook[j+1], listBook[j]
        return listBook

    #OPTION 6
    def check_out_book_func(self):
        print("Welcome to the Check Out page, please login to continue.")
        success = self.login_func()
        if success[0] == False:
            print("Login unsuccessful, the user does not exists.")
            return False
        else:
            with open("ListOfBooks.txt", "a+") as file:
                file.seek(0)
                data = file.readlines()
                bookLists = []
                for book in data:
                    book = book.split("-")
                    LastItem = book.pop()
                    Last = ""
                    for char in LastItem:
                        if char == "\n":
                            continue
                        else:
                            Last += char
                    book.append(Last)
                    bookLists.append(book)
                file.close()
            print("The following books are available in the library: ")
            for book in range(len(bookLists)):
                print("Book Serial Number: ", book + 1)
                print(f" " * 20 + f"{bookLists[book][0]}")
                print("Author Of The Book: ")
                print(f" " * 20 + f"{bookLists[book][1]}")
                print("Stock Of The Book Available: ")
                print(f" " * 20 + f"{bookLists[book][2]}")
                print("Genre Of The Book: ")
                print(f" " * 20 + f"{bookLists[book][3]}")
                print("_" * 50)
            print()
            bookNo = int(input("Enter number of the book you want to borrow: "))
            bookNo -= 1
            borrowBook = bookLists[bookNo]
            bookLists.remove(borrowBook)
            newStock = int(borrowBook[2]) - 1
            updatedBook = [borrowBook[0], borrowBook[1], str(newStock), borrowBook[3]]
            bookLists.append(updatedBook)
            with open("ListOfBooks.txt", "w+") as file:
                for book in bookLists:
                    if book != bookLists[-1]:
                        toWrite = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                        file.write(toWrite + "\n")
                    else:
                        toWrite = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                        file.write(toWrite)
            with open("InfoOfBooks.txt", "a+") as file:
                file.write("\n")
                file.write(success[1]+"-check_out-"+updatedBook[0])
            print("You've borrowed the book successfully.")
            print()


    #OPTION 7
    def renew_book_func(self):
        print("Welcome to the renew page, please login to continue.")
        succ = self.login_func()
        if succ[0] == False:
            print("Login unsuccessful, the user does not exists.")
            return False
        else:
            with open("InfoOfBooks.txt", "a+") as file:
                file.seek(0)
                data = file.readlines()
                bookInfo = []
                for info in data:
                    info = info.split("-")
                    LastItem = info.pop()
                    Last = ""
                    for char in LastItem:
                        if char == "\n":
                            continue
                        else:
                            Last += char
                    info.append(Last)
                    bookInfo.append(info)
                file.close()
            bookName = input("Enter the book name you want to renew: ")
            for info in bookInfo:
                if (succ[1] == info[0]) and (info[1] == "check_out") and (info[2] == bookName):
                    bookInfo.remove(info)
                    print("Thank You for renewing the book. Have a great day!")
                    print()
                    with open("ListOfBooks.txt", "a+") as file:
                        file.seek(0)
                        data = file.readlines()
                        bookLists = []
                        for info in data:
                            info = info.split("-")
                            LastItem = info.pop()
                            Last = ""
                            for char in LastItem:
                                if char == "\n":
                                    continue
                                else:
                                    Last += char
                            info.append(Last)
                            bookLists.append(info)
                        file.close()
                    with open("InfoOfBooks.txt", "w+") as file:
                        file.write(succ[1] + "-renew-" + bookName)
                        file.write("\n")
                        for info in bookInfo:
                            if info != bookInfo[-1]:
                                toWrite = info[0]+"-"+info[1]+"-"+info[2]
                                file.write(toWrite + "\n")
                            else:
                                toWrite = info[0]+"-"+info[1]+"-"+info[2]
                                file.write(toWrite)
                                return


    #OPTION 8
    def reserve_book_func(self):
        print("Welcome to the reserve page, please login to continue.")
        succ = self.login_func()

        if succ[0] == False:
            print("Login unsuccessful, the user does not exists.")
            return False
        else:
            bookName = input("Enter the book name you want to reserve: ")
            with open("InfoOfBooks.txt","a+") as file:
                file.write("\n")
                file.write(succ[1] + "-reserve-" + bookName)
            print("The following book has been reserved successfully.")
            print()


    #OPTION 9
    def return_book_func(self):
        print("Welcome to the Reserve page, please login to continue.")
        success = self.login_func()
        if success[0] == False:
            print("Login unsuccessful, the user does not exists.")
            return False
        else:
            with open("InfoOfBooks.txt", "a+") as file:
                file.seek(0)
                data = file.readlines()
                bookInfo = []
                for info in data:
                    info = info.split("-")
                    LastItem = info.pop()
                    Last = ""
                    for char in LastItem:
                        if char == "\n":
                            continue
                        else:
                            Last += char
                    info.append(Last)
                    bookInfo.append(info)
                file.close()
            bookName = input("Enter the title of the book you want to return: ")
            for info in bookInfo:
                if (success[1] == info[0]) and ((info[1] == "check_out") or (info[1] == "renew")) and (info[2] == bookName):
                    bookInfo.remove(info)
                    print("Thank You for returning the book. Have a great day!")
                    print()
                    with open("ListOfBooks.txt", "a+") as file:
                        file.seek(0)
                        data = file.readlines()
                        bookLists = []
                        for info in data:
                            info = info.split("-")
                            LastItem = info.pop()
                            Last = ""
                            for char in LastItem:
                                if char == "\n":
                                    continue
                                else:
                                    Last += char
                            info.append(Last)
                            bookLists.append(info)
                        file.close()
                    returnBook = None
                    for info in bookLists:
                        if info[0] == bookName:
                            returnBook = info
                    newStock = int(returnBook[2]) + 1
                    updatedBook = [returnBook[0], returnBook[1], str(newStock), returnBook[3]]
                    bookLists.append(updatedBook)
                    with open("ListOfBooks.txt", "w+") as file:
                        for info in bookLists:
                            if info != bookLists[-1]:
                                toWrite = info[0] + "-" + info[1] + "-" + info[2] + "-" + info[3]
                                file.write(toWrite + "\n")
                            else:
                                toWrite = info[0] + "-" + info[1] + "-" + info[2] + "-" + info[3]
                                file.write(toWrite)
                    with open("InfoOfBooks.txt", "w+") as file:
                        for info in bookInfo:
                            if info != bookInfo[-1]:
                                toWrite = info[0]+"-"+info[1]+"-"+info[2]
                                file.write(toWrite + "\n")
                            else:
                                toWrite = info[0]+"-"+info[1]+"-"+info[2]
                                file.write(toWrite)
                                return

    #OPTION 10
    def add_book_func(self):
        with open("ListOfBooks.txt", "a+") as file:
            file.seek(0)
            data = file.readlines()
            bookAdd = []
            for book in data:
                book = book.split("-")
                LastItem = book.pop()
                Last = ""
                for char in LastItem:
                    if char == "\n":
                        continue
                    else:
                        Last += char
                book.append(Last)
                bookAdd.append(book)
            file.close()
        print("The following books are available in the library: ")
        for book in bookAdd:
            print("Title Of The Book: ")
            print(f" "*20 + f"{book[0]}")
            print("Author Of The Book: ")
            print(f" " * 20 + f"{book[1]}")
            print("Stock Of The Book Available: ")
            print(f" " * 20 + f"{book[2]}")
            print("Genre Of The Book: ")
            print(f" " * 20 + f"{book[3]}")
            print("_"*50)
        print()
        bookName = input("Enter the book\'s title: ")
        authorName = input("Enter the name of book\'s author: ")
        stock = int(input("Enter the quantity you want to be in stock: "))
        genre = input("Enter the genre of the book: ")
        with open("ListOfBooks.txt", "a") as file:
            toAdd = bookName+"-"+authorName+"-"+str(stock)+"-Genre "+str(genre)
            file.write("\n")
            file.write(toAdd)
        print("The book has been added successfully in the library.")
        print()


    #OPTION 11
    def remove_book_func(self):
        with open("ListOfBooks.txt", "a+") as file:
            file.seek(0)
            data = file.readlines()
            bookSub = []
            for book in data:
                book = book.split("-")
                LastItem = book.pop()
                Last = ""
                for char in LastItem:
                    if char == "\n":
                        continue
                    else:
                        Last += char
                book.append(Last)
                bookSub.append(book)
            file.close()
        print("The following books are available in the library: ")
        for book in bookSub:
            print("Title Of The Book: ")
            print(f" " * 20 + f"{book[0]}")
            print("Author Of The Book: ")
            print(f" " * 20 + f"{book[1]}")
            print("Stock Of The Book Available: ")
            print(f" " * 20 + f"{book[2]}")
            print("Genre Of The Book: ")
            print(f" " * 20 + f"{book[3]}")
            print("_" * 50)
        print()
        bookName = input("Enter the title of the book you want to remove: ")
        stock = int(input("Enter the quantity you want to remove: ")) # quantity must be less than total no.of existing books
        toSub = ""
        for book in bookSub:
            if book[0] == bookName:
                toSub = book
                break
        bookSub.remove(toSub)
        if int(toSub[2]) - stock == 0:
            pass
        else:
            newStock = int(toSub[2]) - stock
            bookToWrite = [toSub[0], toSub[1], str(newStock), toSub[3]]
            bookSub.append(bookToWrite)
        with open("ListOfBooks.txt", "w+") as file:
            for book in bookSub:
                if book != bookSub[-1]:
                    toWrite = book[0]+"-"+book[1]+"-"+book[2]+"-"+book[3]
                    file.write(toWrite+"\n")
                else:
                    toWrite = book[0] + "-" + book[1] + "-" + book[2] + "-" + book[3]
                    file.write(toWrite)
        print("The following book has been removed.")
        print()


    #OPTION 12
    def cancel_membership_func(self):
        print("Please fill the following to cancel your membership: ")
        email = input("Enter your email: ")
        pw = input("Enter your password: ")
        with open("ListOfUsers.txt", "r+") as file:
            file.seek(0)
            data = file.readlines()
            listUser = []
            for user in data:
                user = user.split("-")
                LastItem = user.pop()
                Last = ""
                for char in LastItem:
                    if char == "\n":
                        continue
                    else:
                        Last += char
                user.append(Last)
                listUser.append(user)
        toSub = [email, pw]
        if toSub in listUser:
            listUser.remove(toSub)
        with open("ListOfUsers.txt", "w+") as file:
            for user in listUser:
                if user != listUser[-1]:
                    toWrite = user[0] + "-" + user[1]
                    file.write(toWrite + "\n")
                else:
                    toWrite = user[0] + "-" + user[1]
                    file.write(toWrite)
            return
        print("Your membership has been cancelled.")
        print()


                                                #DRIVER CODE

objectt = Library_Management()
print("                                    WELCOME TO ST. LOUIS COUNTY LIBRARY")
print()
while True:
    print("""YOU CAN PERFORM THE FOLLOWING FUNCTIONS:
1. Login
2. Signup 
3. Edit a Book
4. Search a Book
5. Display all Books
6. Check-Out or Borrow a Book
7. Renew a Book
8. Reserve a Book
9. Return a Book
10. Add a Book
11. Remove a Book
12. Cancel Membership
13. Logout
                """)
    n = int(input("Enter the step you want to choose: "))
    print()
    if n == 13:
        print("THANKYOU FOR VISITING THE ST. LOUIS COUNTY LIBRARY.")
        print('*'*50)
        break
    if n == 1:
        objectt.login_func()
    if n == 2:
        objectt.signup_func()
    if n == 3:
        objectt.edit_book_func()
    if n == 4:
        r=objectt.search_book_func()
        print()
        print("Item you've searched for:")
        print()
        for item in r:
            print("BOOK NAME: ",item[0])
            print("AUTHOR NAME: ",item[1])
            print("AVAILABLE IN STOCK: ",item[2])
            print("GENRE: ",item[3])
            print()
    if n == 5:
        objectt.display_records_func()
    if n == 6:
        objectt.check_out_book_func()
    if n == 7:
        objectt.renew_book_func()
    if n == 8:
        objectt.reserve_book_func()
    if n == 9:
        objectt.return_book_func()
    if n == 10:
        objectt.add_book_func()
    if n == 11:
        objectt.remove_book_func()
    if n == 12:
        objectt.cancel_membership_func()
    
