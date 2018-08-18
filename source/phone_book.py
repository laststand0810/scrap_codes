class PhoneBook:
    def __init__(self, book_log=1000):
        '''
        init of PhoneBook
        :param book_log: int, length of the PhoneBook, limited between 1 and 100000.
        '''
        if book_log not in range(1, 100000):
            print("phone book must be between 1 to 100000 in length.")
            del self
            return
            raise ValueError("phone book must be between 1 to 100000 in length.")
        print("create Phone Book with size %d" % book_log)
        self.catalogue = {}
        self.book_log = book_log

    def add_contact(self, name, phone_num):
        '''
        add contact to phone book.
        :param name: str, name of the contact.
        :param phone_num: str, phone number.
        :return: None
        '''
        if name in self.catalogue: # check for update.
            print("update %s info: %s" % (name, phone_num))
            self.catalogue[name] = phone_num
        elif len(self.catalogue) < self.book_log: # check for length exceed.
            print("add %s info: %s" % (name, phone_num))
            self.catalogue[name] = phone_num
        else:
            print("Error: exceed book log length")

    def search_contact(self, name):
        '''
        search for the contact info.
        :param name: str, name of the contact
        :return: None
        '''
        try:
            print("Contact of {0} is: {1}".format(name, self.catalogue[name]))
        except KeyError:
            print("Not found")

    def print_book(self):
        '''
        print the book.
        :return: None
        '''
        print("{:+^20}".format("Log Book"))
        for name, contact in sorted(self.catalogue.items()):
            print("{0:-<10}{1:->10}".format(name, contact))
        print("{:+^20}".format(""))

# Create sample phonebook
book = PhoneBook(5)
# Add contacts
book.add_contact("Cathy", "09001679")
book.add_contact("John", "09003942")
book.add_contact("Mary", "09011425")
book.add_contact("Colson", "09001111")
book.add_contact("Niel", "09002345")
book.add_contact("Poplar", "09004058")
book.add_contact("Whister", "09001238")
# Add existing contact
book.add_contact("Cathy", "11111111")
# Present book
book.print_book()
# Search contact (exist/nonexist)
book.search_contact("Mary")
book.search_contact("Doug")

# Create sample phonebook exceed range
second_book = PhoneBook(100001)
# Try printing the object to see if it still exist
print(second_book)
