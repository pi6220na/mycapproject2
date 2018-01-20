# Project 2 - Book Wish List
# Issue #2 - Separate file io into a new module.
# Jeremy Wolfe 1/19/2018

import os, datastore, json


DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

book_list = []


def setup():
    ''' Read book info from file, if file exists. '''

    global counter

    try :
        with open(BOOKS_FILE_NAME) as f:
            #data = f.read()
            data = json.load(f)
            print(data)
            print('')
            datastore.make_book_list(data)


    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass


    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                counter = int(f.read())
            except:
                print('problem reading counter.txt file')
                counter = 0
    except:
        counter = len(book_list)

    #print('in fileio setup, counter = ' + str(counter))
    return counter

def shutdown(counter):
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = datastore.make_output_data()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        json.dump(output_data, f)

    with open(COUNTER_FILE_NAME, 'w') as f:
        print('writing counter to file = ' + str(counter))
        f.write(str(counter))

