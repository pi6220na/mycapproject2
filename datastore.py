
import os, fileio, json
from book import Book

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    #Jeremy debugging
    #print('entering get_books. kwargs = ' + str(kwargs))
    #for item in book_list:
    #    print(item)


    if len(kwargs) == 0:
        return book_list

    if kwargs['read']:
        k_string = 'True'
    else:
        k_string = 'False'

    if 'read' in kwargs:
        #print('within the if "read" in kwargs')
        #print(kwargs['read'])
        read_books = [ book for book in book_list if book.read == k_string ]
        return read_books



def add_book(book):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.id = generate_id()
    book_list.append(book)


def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, read):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.read = True
            return True

    return False # return False if book id is not found



def make_book_list(string_from_file):
    ''' turn the string from the file into a list of Book objects'''

    global book_list

    #Jeremy debugging
    #print('string_from_file = ' + string_from_file)

    myJSON = json.JSONDecoder().decode(string_from_file)

    #print('myJSON = ' + str(myJSON))

    for book_str in myJSON:
        book = Book(book_str['book'],book_str['author'],book_str['beenRead'],book_str['bookID'])
        book_list.append(book)

    #for item in book_list:
    #    print(item)

def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    #reformat a book object into JSON format
    for book in book_list:
        output_str = { 'book': book.title, 'author':book.author, 'beenRead':str(book.read), 'bookID':str(book.id) }
        output_data.append(output_str)

    #convert output_data into JSON
    myJSON = json.JSONEncoder().encode(output_data)

    return myJSON
