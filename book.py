class Book(object):

    ''' Represents one book in a user's list of books'''

    NO_ID = -1

    #def __init__(self, title, author, r_date, rating, read=False, id=NO_ID):
    def __init__(self, title, author, read, r_date, rating, id):
        '''Default book is unread, and has no ID'''
        #primary constructor
        self.title = title      #string
        self.author = author    #string
        self.read = read        #boolean
        self.dateRead = r_date  #date
        self.rating = rating    #integer 1 - 5
        self.id=id              #integer incremented in book added sequence

    # alternate constructor
    #@classmethod
    #def make_book(self, title, author, read, r_date, rating, id):
    #    self.title = title      #string
    #    self.author = author    #string
    #    self.read = read        #boolean
    #    self.dateRead = r_date  #date
    #    self.rating = rating    #integer 1 - 5
    #    self.id=id              #integer incremented in book added sequence
    #    print('printing from within the make book class method: title and author: ' + self.title, self.author)
    #    return self

    def set_id(self, id):
        self.id = id


    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'

        #Jeremy
        #print('in book.py string print read = ' + str(self.read) + ' read_str = ' + read_str)

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        template = 'Title: {} Author: {} Read: {} Date Read: {} Rating: {} id: {} '
        return template.format(self.title, self.author, read_str, self.dateRead, self.rating, id_str)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read \
               and self.id==other.id and self.dateRead == other.date_read and self.rating == other.rating




