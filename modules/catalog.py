from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd

class Catalog():
    def __init__(self, catalog=None):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog in self.catalog:
            for item in catalog:
                if input_search in item.title.lower():
                    if type(item) == Magazine:
                        list_result.append('Title: ' + item.title + 'Volume: ' + item.volume + 'Type Catalog: Magazine')
                    elif type(item) == Book:
                        list_result.append('Title: ' + item.title + 'DDS_Number: ' + item.dds_number + 'Type Catalog: Book')
                    elif type(item) == Dvd:
                        list_result.append('Title: ' + item.title + 'Genre: ' + item.genre + 'Type Catalog: DVD')
                    elif type(item) == Cd:
                        list_result.append('Title: ' + item.title + 'Artist: ' + item.artist + 'Type Catalog: CD')
                    else:
                        pass
        return list_result