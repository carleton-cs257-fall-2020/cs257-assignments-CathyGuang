#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 26 September 2020

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2020.

    Author format:

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}
        {'id': 134, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Book format:

        {'title': 'A Wild Sheep Chase', 'publication_year': 1982, 'author_id': 134}
'''

import csv

class BooksDataSource:
    def __init__(self, books_csv_file_name, authors_csv_file_name):
        ''' The books CSV file format:

                author_id,title,publication_year
                4,Jane Eyre,1847
                22,Bleak House,1852

            The authors CSV file format:
                id,last_name,first_name,birth_year,death_year
                23,Carré,John Le,1931,NULL
                18,DuMaurier,Daphne,1907,1989

            NULL is used in the CSV to represent a future/unknown death year.
        '''
        self.book_list = []
        with open(books_csv_file_name) as books_file:
            reader = csv.reader(books_file)
            row = next(reader) # consume the top row and ignore it
            for row in reader:
                book = {'author_id':int(row[0]), 'title':row[1], 'publication_year': int(row[2])}
                self.book_list.append(book)

        self.author_ids = {} # this will help us check an author ID's validity quickly
        self.author_list = []
        with open(authors_csv_file_name) as authors_file:
            reader = csv.reader(authors_file)
            row = next(reader)
            for row in reader:
                death_year = row[4] if row[4] != 'NULL' else None
                author = {'id':int(row[0]), 'last_name':row[1], 'first_name':row[2],
                          'birth_year':int(row[3]), 'death_year':death_year}
                self.author_ids[author['id']] = 0
                self.author_list.append(author)

    def is_valid(self, author_id):
        return author_id in self.author_ids

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year
                
            This method raises a ValueError if author_id is non-None but is not a valid author ID.
        '''
        filtered_books = []
        for book in self.book_list:
            if author_id is not None and not self.is_valid(author_id):
                raise ValueError(f'Invalid author ID {author_id}')
            if author_id is not None and book['author_id'] != author_id:
                continue
            if search_text is not None and search_text.lower() not in book['title'].lower():
                continue
            if start_year is not None and book['publication_year'] < start_year:
                continue
            if end_year is not None and book['publication_year'] > end_year:
                continue
            filtered_books.append(book)

        if sort_by == 'year':
            filtered_books = sorted(filtered_books, key=lambda book: book['publication_year'])
        else:
            filtered_books = sorted(filtered_books, key=lambda book: book['title'])

        return filtered_books.copy()

    def authors(self, search_text=None):
        ''' Returns a list of all the authors in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then authors
            returns all of the authors, sorted by birth year.
        '''
        filtered_authors = []
        for author in self.author_list:
            name = author['first_name'] + ' ' + author['last_name']
            if search_text is not None and search_text.lower() not in name.lower():
                continue
            filtered_authors.append(author)
        filtered_authors = sorted(filtered_authors, key=lambda author: author['birth_year'])
        return filtered_authors.copy()

