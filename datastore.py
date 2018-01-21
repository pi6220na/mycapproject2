from book import Book
import datetime, json
import pprint

pp = pprint.PrettyPrinter(indent=4)

# convert a date string into a date
# command line -  pip install python-dateutil  #http://labix.org/python-dateutil
# https://stackoverflow.com/questions/466345/converting-string-into-datetime
from dateutil import parser

book_list = []
counter = 0

def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    read_books = []
    #Jeremy debugging
    #print('entering get_books. kwargs = ' + str(kwargs))

    #json.dumps(book, indent=4, sort_keys=True)
    #json.dumps(book_list, indent=4)

    if len(kwargs) == 0:
        return book_list

    #print(type(book_list))
    #for book in book_list:
    #    print(type(book))

    if 'read' in kwargs:
        for book in book_list:
            #print(book.read)
            #print(type(book))
            #print(kwargs['read'])
            #if (book.read == kwargs['read']):
            if (book.read == True and kwargs['read'] == True):
                read_books.append(book)
            elif (book.read == False and kwargs['read'] == False):
                read_books.append(book)

        return read_books

    #print(kwargs['search'])
    if 'search' in kwargs:
        for book in book_list:
            #print(book.id)
            #print(book.title)
            #print(book.author)

            if (book.title == kwargs['search']):
                return book

        return 'not found'



def add_book(book, counter):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.id = generate_id(counter)
    counter = book.id
    #print('book.id = ' + str(book.id) + ' counter = ' + str(counter))
    book_list.append(book)
    return counter


def generate_id(counter):
    counter += 1
    return counter


def set_read(book_id, book_rating):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.read = True
            book.rating = book_rating
            book.dateRead = str(datetime.datetime.now().date())
            return True

    return False # return False if book id is not found


def make_book_list(string_from_file):
    ''' turn the string from the file into a list of Book objects'''

    #print('entering make_book_list')

    global book_list

    book_list = []

    template = 'Title: {} Author: {} Read: {} Date Read: {} Rating: {} id: {} '

    index = 0

    for book_str in string_from_file:

        bk = Book(book_str['title'], book_str['author'], book_str['read'],
                            book_str['dateRead'], book_str['rating'], book_str['id'])

        #print(type(bk))
        book_list.append(bk)

    #print('printing the book_list')
    #for bk in book_list:
    #    print(template.format(bk.title, bk.author, bk.read, bk.dateRead, bk.rating, bk.id))


def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    #reformat a book object into JSON format
    for book in book_list:
        output_str = { 'title': book.title, 'author':book.author, 'read':(book.read),
                       'dateRead':str(book.dateRead), 'rating':(book.rating), 'id':(book.id) }
        output_data.append(output_str)

    return output_data

def sort_the_list(mySort):
    '''sort the book_list based on the user's choice for sort order'''

    global book_list

    if mySort == 't':
        sorted_list = sorted(book_list, key=lambda book: book.title)  # sort by title
        print('book list sorted on title')
    else:
        sorted_list = sorted(book_list, key=lambda book: book.author)  # sort by author
        print('book list sorted on author')

    book_list = sorted_list
    return book_list
