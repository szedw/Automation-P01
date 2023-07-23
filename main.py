from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.catalog import Catalog
import json

book_1 = Book('Title Test 1', 'Ini Subject Test 1', None, '1345-24533', 'Edward', '1234567890')
book_2 = Book('Title Test 2', 'Ini Subject Test 2', None, '1345-24533', 'Davina', '1234567890')

magazine_1 = Magazine('media cnn', 'edisi 14 Juli 2023', None, 'Volume 1', '-')
magazine_2 = Magazine('media cnbc', 'edisi 15 Juli 2023', None, 'Volume 1', '-')

dvd_1 = Dvd('Test Dvd 1', 'ini subject dvd 1', None, None, None, 'Drama')

##input search
#input_search = 'test'

#collect data per category
book = [book_1, book_2]
magazine = [magazine_1, magazine_2]
dvd = [dvd_1]

#collect all data
catalog_all = [book, magazine, dvd]

#for catalog in catalog_all:
#    for item in catalog:
#        if input_search in item.title.lower():
#            if type(item) == Magazine:
#                print('Title: ', item.title, 'Volume: ', item.volume, 'Type Catalog: Magazine')
#            elif type(item) == Book:
#                print('Title: ', item.title, 'Dds_number: ', item.dds_number, 'Type Catalog: Book')
#            elif type(item) == Dvd:
#                print('Title: ', item.title, 'Genre: ', item.genre, 'Type Catalog: Dvd')
#            elif type(item) == Cd:
#                print('Title: ', item.title, 'Artist: ', item.artist, 'Type Catalog: Cd')
#            else:
#                pass

# #input & result
# input_search = 'test'
# results = Catalog(catalog_all).search(input_search)
# for index, result in enumerate(results):
#     print(f'result ke-{index+1} | {result}')


#get data from json
f = open('files/catalog.json')
data_json = json.load(f)
#create object from data json
for item in data_json:
    if item['source'] == 'book':
        book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            isbn=item['isbn'],
            authors=item['authors'],
            dds_number=item['dds_number']))
    elif item['source'] == 'magazine':
        magazine.append(Magazine(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume=item['volume'],
            issue=item['issue']))    
    elif item['source'] == 'dvd':
        dvd.append(Dvd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            actors=item['actors'],
            director=item['director'],
            genre=item['genre']))
    elif item['source'] == 'cd':
        cd.append(Cd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            artist=item['artist'])) 
    else:
        pass

#input & result
input_search = 'test'
results = Catalog(catalog_all).search(input_search)
for index, result in enumerate(results):
    print(f'result ke-{index+1} | {result}')