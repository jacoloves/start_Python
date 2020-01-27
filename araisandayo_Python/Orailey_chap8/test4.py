import csv
with open('books', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    books = [row for row in cin]

print(books)