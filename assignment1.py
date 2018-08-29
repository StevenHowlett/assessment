"""
Replace the contents of this module docstring with your own details
Name: Steven Howlett
Date started:26/08/2018
GitHub URL:
"""


def main():
    print("Reading Tracker 1.0 - by Steven Howlett")

    file_location="temp.csv"
    input_file=open(file_location,"r")
    books_loaded=0
    information_to_book={}
    for line in input_file:
        line=line.strip()
        book_details =line.split(',')
        key = book_details.pop(0)
        information_to_book[key] =book_details
        books_loaded +=1
    print("{} books loaded from {}".format(books_loaded,file_location))


    menu_choice = input("Menu:\nL = List all books\nA = Add new book\nM = Mark a new book as completed\nQ = Quit\n>>>").lower()
    while menu_choice != "q":
        if menu_choice == "l":
            if list_book_details(information_to_book):
                print('No more books left to read. Why not add a new book?')
            menu_choice = input("Menu:\nL = List all books\nA = Add new book\nM = Mark a new book as completed\nQ = Quit\n>>>").lower()


        else:
            print("invalid input")
            menu_choice = input("Menu:\nL = List all books\nA = Add new book\nM = Mark a new book as completed\nQ = Quit\n>>>").lower()




def list_book_details(book_to_information):
    book_names = book_to_information.keys()
    book_names = sorted(book_names)
    authors=[]
    amounts_of_pages=[]
    book_completes=[]
    largest_author_length=0
    largest_book_name_length=0

    for book in book_names:
        book_information=book_to_information[book]
        authors.append(book_information[0])
        amounts_of_pages.append(int(book_information[1]))
        book_completes.append(book_information[2])
        if len(book_information[0]) > largest_author_length:
            largest_author_length=len(book_information[0])
        if len(book)>largest_book_name_length:
            largest_book_name_length=len(book)
    total_unread_pages =0
    total_unread_books =0
    if len(book_completes) == 0:
        return True
    for i in range(0,len(book_names)):
        book_complete=" "
        if book_completes[i] == 'r':
            book_complete="*"
            total_unread_pages += amounts_of_pages[i]
            total_unread_books += 1
        print("{}{}. {:<{}}  by {:<{}} {:>4} pages".format(book_complete,i+1,book_names[i],largest_book_name_length,authors[i],largest_author_length,amounts_of_pages[i]))


    print("{} books.".format(len(book_names)))
    print("you need to read {} pages in {} books".format(total_unread_pages,total_unread_books))
    return False

if __name__ == '__main__':
    main()
