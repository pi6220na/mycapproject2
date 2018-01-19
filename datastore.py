from book import Book

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

    if 'read' in kwargs:
        read_books = [ book for book in book_list if book.read == kwargs['read'] ]
        return read_books


def add_book(book, counter):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.id = generate_id(counter)
    counter = book.id
    print('book.id = ' + str(book.id) + ' counter = ' + str(counter))
    book_list.append(book)
    return counter


def generate_id(counter):
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

    for book_str in string_from_file:
        book = Book(book_str['book'],book_str['author'],book_str['beenRead'],book_str['bookID'])
        book_list.append(book)


def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    #reformat a book object into JSON format
    for book in book_list:
        output_str = { 'book': book.title, 'author':book.author, 'beenRead':(book.read), 'bookID':(book.id) }
        output_data.append(output_str)

    return output_data
