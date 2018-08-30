"""
Name: Steven Howlett
Date started:26/08/2018
GitHub URL: personal https://github.com/StevenHowlett/assessment ,
            class https://github.com/CP1404-2018-2/a1-StevenHowlett/tree/master
            (2 copys because of committing mistake ,personal has more commits)

Program reads books and their information from a csv file, allows user to view a list of books,
mark books as completed and add new books. the program then rewrites the csv file with an updated list of books.
"""
FILE_LOCATION = "books.csv"
MENU = "Menu:\nL = List all books\nA = Add new book\nM = Mark a new book as completed\nQ = Quit\n>>>"

"""main calls other functions and loops the program while the user has not entered q """


def main():
    print("Reading Tracker - by Steven Howlett")

    book_to_information = load_books_from_file()

    menu_choice = input(MENU).lower()
    while menu_choice != "q":
        while menu_choice == "l":
            list_book_details(book_to_information)
            if not does_contain_required_book(book_to_information):
                print('No more books left to read. Why not add a new book?')
            menu_choice = input(MENU).lower()
        while menu_choice == "m":
            if not does_contain_required_book(book_to_information):
                print("There are no required books")
            else:
                list_book_details(book_to_information)
                book_to_information = mark_book_as_complete(book_to_information)
            menu_choice = input(MENU).lower()
        while menu_choice == "a":
            add_new_book(book_to_information)
            menu_choice = input(MENU).lower()
        else:
            print("invalid input")
            menu_choice = input(
                "Menu:\nL = List all books\nA = Add new book\nM = Mark a new book as completed\nQ = Quit\n>>>").lower()

    save_books_to_file(book_to_information)


"""overwrites the file with keys and values from book_to_information"""


def save_books_to_file(book_to_information):
    output_file = open(FILE_LOCATION, "w")
    for book in book_to_information.keys():
        book_information = book_to_information[book]
        print("{},{},{},{}".format(book, book_information[0], book_information[1], book_information[2]),
              file=output_file)
    print("{} books saved today\n have a nice day :)".format(len(book_to_information.keys())))


"""gets input from the user and adds a book to book_to_information"""


def add_new_book(book_to_information):
    is_valid = False
    while not is_valid:
        book_name = input('Title:')
        is_valid = error_check_text(book_name)
    is_valid = False
    while not is_valid:
        author = input('Author:')
        is_valid = error_check_text(author)
    is_valid = False
    while not is_valid:
        try:
            number_of_pages = int(input("Pages:"))
            if number_of_pages < 1:
                print("must have at least 1 page")
            else:
                is_valid = True
        except ValueError:
            print("Invalid Input; enter a valid number")
    book_to_information[book_name] = [author, number_of_pages, 'r']
    print('{} by {} ,({} pages) added to reading tracker'.format(book_name, author, number_of_pages))
    print(book_to_information)


"""error checks for text inputs in add_new_book"""


def error_check_text(user_text):
    is_valid = False
    if user_text == ' ' or '':
        print("input cannot be blank")
    else:
        is_valid = True
    return is_valid


"""finds a book from the user input and changes it from required to completed"""


def mark_book_as_complete(book_to_information):
    books = sorted(book_to_information.keys())
    is_valid = False
    while not is_valid:
        try:
            book_number = int(
                input("Enter the number of the book you would like to mark as completed\n>>>")) - 1
            book_name = books[book_number]
            book_information = book_to_information[book_name]
            if book_number > len(books):
                print('invalid book number')
            if book_information[2] == 'c':
                print('that book is already completed')
            if book_number < 0:
                print('Number must be > 0')
            is_valid = True
        except ValueError:
            print("Invalid input; enter a valid number")
    book_information[2] = 'c'
    book_to_information[book_name] = book_information
    print("{} by {} completed.".format(book_name, book_information[0]))
    return book_to_information


"""check if there are any books that are required"""


def does_contain_required_book(book_to_information):
    for book in book_to_information.keys():
        book_information = book_to_information[book]

        if book_information[2] == 'r':
            return True
    return False


"""reads from csv file and stores information in book_to_information"""


def load_books_from_file():
    input_file = open(FILE_LOCATION, "r")
    books_loaded = 0
    information_to_book = {}
    for line in input_file:
        line = line.strip()
        book_details = line.split(',')
        book_name = book_details.pop(0)
        information_to_book[book_name] = book_details
        books_loaded += 1
    print("{} books loaded from {}".format(books_loaded, FILE_LOCATION))
    input_file.close()
    return information_to_book


"""displays a list of books and their; authors ,pages and if they are required or completed. also displays number of required books and the sum of pages for those books"""


def list_book_details(book_to_information):
    book_names = book_to_information.keys()
    book_names = sorted(book_names)
    authors = []
    amounts_of_pages = []
    book_completes = []
    largest_author_length = 0
    largest_book_name_length = 0

    for book in book_names:
        book_information = book_to_information[book]
        authors.append(book_information[0])
        amounts_of_pages.append(int(book_information[1]))
        book_completes.append(book_information[2])
        if len(book_information[0]) > largest_author_length:
            largest_author_length = len(book_information[0])
        if len(book) > largest_book_name_length:
            largest_book_name_length = len(book)
    total_unread_pages = 0
    total_unread_books = 0
    for i in range(0, len(book_names)):
        book_complete = " "
        if book_completes[i] == 'r':
            book_complete = "*"
            total_unread_pages += amounts_of_pages[i]
            total_unread_books += 1
        print(
            "{}{}. {:<{}}  by {:<{}} {:>4} pages".format(book_complete, i + 1, book_names[i], largest_book_name_length,
                                                         authors[i], largest_author_length, amounts_of_pages[i]))

    print("{} books.".format(len(book_names)))
    print("you need to read {} pages in {} books".format(total_unread_pages, total_unread_books))
    return False


if __name__ == '__main__':
    main()
