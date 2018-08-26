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

    valid_menu_choice=["l","a","m","q"]
    menu_choice=input("Menu:\nL = List all books\nA = Add new book\nM = Mark a new book as completed\nQ = Quit\n>>>").lower()
    while not menu_choice in valid_menu_choice:
        print("invalid menu choice")
        menu_choice=input("Menu:\nL = List all books\nA = Add new book\nM = Mark a new book as completed\nQ = Quit").lower()



if __name__ == '__main__':
    main()
