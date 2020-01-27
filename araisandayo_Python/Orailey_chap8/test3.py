import csv
members = [
    ['author', 'book'],
    ['J R R Tolkien', 'The Hobbit'],
    ['Lynne Truss', '\"Eats, Shoots & Leaves\"']
]

with open('books', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(members)