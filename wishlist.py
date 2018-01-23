# Main program
# Project 2 - Book Wish List

# Issue #9 Add the ability to delete a book from the wishlist
# Nnamdi Keshi 1/21/2018

# Issue #1 Create a README.md file
# Nnamdi Keshi 1/22/2018

# Issue #6 Alert if a book that has been read, is added to the wishlist
# Nnamdi Keshi 1/22/2018

# Issue #8 Add the ability to edit a book's title and/or author
# Nnamdi Keshi 1/22/2018

# Issue #2 Sepatate file IO into a new module (fileio.py)
# Jeremy Wolfe 1/21/2018

# Issue #3 Save the book data as JSON
# Jeremy Wolfe 1/21/2018

# Issue #5 Save a rating or review of a book that has been read
# Jeremy Wolfe 1/21/2018

# Issue #7 Sort the list of books by title or author
# Jeremy Wolfe 1/21/2018

# Issue #10 Save the date a book was read
# Jeremy Wolfe 1/21/2018


import ui, datastore, fileio


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        sort_books()

    elif choice == '6':
        search_books()
        
    elif choice == '7':
        edit_books()
        
    elif choice == '8':
        delete_books()
        
    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error, get decision for re-read'''
    book_id = ui.ask_for_book_id()
    book_rating = ui.ask_for_book_rating()
    
    if datastore.set_read(book_id, book_rating):
        ui.message('Successfully updated')
        
        while True:
            againWish=input("\nQuick Question..\nDo you want to add this book back into your wishlist for future reading? 'y'es or 'n'o ").strip().lower()
            if againWish =="y":
                new_book()
                print ("*Successfully Added to wishlist*\n")
                break
                
            elif againWish != "y":
                break            
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    global counter

    new_book = ui.get_new_book_info()

    #print('in new_book')
    #print(new_book)

    counter = datastore.add_book(new_book, counter)
    ui.message('Book added: ' + str(new_book))


def sort_books():
    '''Sort books in Title or Author sequence based on user input'''

    mySort = ui.get_sort_order()
    datastore.sort_the_list(mySort)


def search_books():
    '''Search for a user specified book title and notify the user if found'''

    mySearch = ui.get_search_string()
    searchResult = datastore.get_books(search=mySearch)
    if searchResult != 'not found':
        print('This book was found: ', searchResult)
    else:
        print('The book was NOT found')

def edit_books():
    ''' Search for book by ID, notify if update successful '''
    book_id = ui.ask_for_book_id()
    if datastore.edit_book(book_id):
        ui.message('Successfully updated')
    else:
        ui.message('The book was NOT found')
        
def delete_books():
    '''Search for a user specified book title to to delete'''
    
    global book_list
    global counter
    mySearch = ui.get_search_string()
    searchResult = datastore.get_books(search=mySearch)
    
    if searchResult != 'not found':
        while True:
            confirm=input("Book Found.\nDo you really want to delete this book? 'y'es or 'n'o ").strip().lower()
            if confirm.lower() =="y":
                #position = fileio.book_list.index(str(searchResult))
                #print(position)
                
                #removed = fileio.book_list.pop(position)
                removed = datastore.delete_book(searchResult)
                
                #print ("Successfully Deleted:", searchResult,"\n")
                print("Successfully Deleted:", removed, "\n")          # changed to print removed - Jeremy
                break
                
            elif confirm != "y":
                break
    else:
        print('The book was NOT found')


def quit():
    '''Perform shutdown tasks'''
    global counter

    #print ('in wishlist.py, about to shutdown, counter = ' + str(counter))

    fileio.shutdown(counter)
    ui.message('Bye!')


def main():
    global counter

    counter = fileio.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
