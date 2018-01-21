from book import Book


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Sort all books
        6. Search for a book title
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def show_list(books):
    ''' Format and display a list of book objects'''

    if len(books) == 0:
        print ('* No books *')
        return

    #print('about to print books')
    template = ' Title: {} Author: {} Read: {} Date Read: {} Rating: {} id: {}'
    for book in books:
         print(template.format(book.title, book.author, book.read, book.dateRead, book.rating, book.id))

    print('* {} book(s) *'.format(len(books)))


def ask_for_book_id():

    ''' Ask user for book id, validate to ensure it is a positive integer '''

    while True:
        try:
            id = int(input('Enter book id:'))
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')


def ask_for_book_rating():
    ''' Get the rating 1 - 5 for a book being marked as read '''

    while True:
        try:
            rate = int(input('Enter a rating for the book, numberic 1 - 5: '))
            if rate >= 0 and rate <= 5:
                return rate
            else:
                print('Please enter a positive number between 1 and 5')
        except ValueError:
            print('Please enter an integer number')



def get_new_book_info():

    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')
    read = False
    date_read = 'None'
    rating = 0
    id = 0
    return Book(title, author, read, date_read, rating, id)


def message(msg):
    '''Display a message to the user'''
    print(msg)

def get_sort_order():
    '''Get the user's choice in sorting the book list'''

    while True:
        try:
            sort_order = input('Enter sort on Title "T" or sort on Author "A" - input "T" or "A": ')

            if sort_order.lower() == 't' or sort_order.lower() == 'a':
                return sort_order.lower()
            else:
                print('Please enter "T" or "A" or "t" or "a"')

        except ValueError:
            print('Please enter a "T" or "A"')

def get_search_string():
    '''get the book title the user wants to search for'''

    return input('Enter the book title you want to search for: ')