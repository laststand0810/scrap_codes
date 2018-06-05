class PhoneBook:
    def __init__(self, book_log = 1000):
        self.catalogue = {}
        self.book_log = book_log

    def add_contact(self, name, phone_num):
        self.catalogue[name] = phone_num

    def search_contact(self, name):
        try:
            print(self.catalogue[name])
        except KeyError:
            print("Not found")

    def print_contact(self):
        print(list(self.catalogue.items()))


book = PhoneBook()
book.add_contact("Cathy", "09001679")
book.add_contact("John", "09003942")
book.add_contact("Mary", "09011425")
book.add_contact("Colson", "09001111")
book.add_contact("Niel", "09002345")
book.add_contact("Poplar", "09004058")
book.add_contact("Whister", "09001238")
book.add_contact("Cathy", "11111111")
book.print_contact()
book.search_contact("Mary")
book.search_contact("Doug")