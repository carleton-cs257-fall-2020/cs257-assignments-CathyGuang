# Alison Cameron and Cathy Guang
# Revised by Cathy Guang
# CS257 Carleton College
# September 25, 2020
# A program to experiment with command line arguments to manipulate a dataset
import csv
import argparse

def search_authors(searchstring):
    '''search_authors(searchstring) will return a dictionary of all authors
    whose names contain the given searchstring (case insensitive),
    as well as all of the books that they have published.'''
    searchstring = searchstring.lower()
    authorbooks_dict = {}

    # open dataset and loop through
    with open('books.csv', 'r') as bookfile:
        reader = csv.reader(bookfile)
        for row in reader:
            author = row[2]
            authorLower = author.lower()
            if searchstring in authorLower:
                if author in authorbooks_dict:
                    authorbooks_dict[author].append(row[0])
                else:
                    authorbooks_dict[author] = [row[0]]

    return authorbooks_dict

def print_authors(authorbooks_dict):
    '''print_authors(authorbooks_dict) will display all authors
    whose names contain the given searchstring (case insensitive),
    as well as all of the books that they have published.'''
    if len(authorbooks_dict) == 0:
        # if there are no matching authors, print an error message.
        print("We couldn't find any authors that matched this search")
    else:
        # for each author in the dictionary, print out all their published books
        for author in authorbooks_dict:
            print("Books written by", author + ":")
            for book in authorbooks_dict[author]:
                print("     ", book)
            print()

def search_titles(searchstring):
    '''search_titles(searchstring) will return a list of all books whose
    titles contain the given searchstring (case insensitive).'''
    searchstring = searchstring.lower()
    title_count = 0
    title_list = []
    # open the dataset and loop through
    with open('books.csv', 'r') as bookfile:
        reader = csv.reader(bookfile)
        for row in reader:
            title = row[0]
            titleLower = title.lower()
            if searchstring in titleLower:
                title_list.append(title)
                title_count += 1
    if title_count == 0:
        #if no book titles match the searchstring, print this error message.
        print("We couldn't find any books that matched this search")

    return title_list

def print_titles(title_list):
    '''search_titles(searchstring) will display all books whose
    titles contain the given searchstring (case insensitive).'''
    for title in title_list:
        print(title)

def find_books_in_range(startyear, endyear):
    '''find_books_in_range(startyear, endyear) will return a dictionary including all books
    whose publication year is within the given inclusive range. Each line will contain
    the title of the book, the author, and the publication date. A Count value is also in
    the dictionary to track if there's any books in publication year range'''
    books_dict = {}
    books_dict["Booklist"] = []
    books_dict["Count"] = 0
    #open the dataset and loop through
    with open('books.csv', 'r') as bookfile:
        reader = csv.reader(bookfile)
        if startyear > endyear:
            books_dict["Error"] = True
        for row in reader:
            published = int(row[1])
            if published >= startyear and published <= endyear:
                books_dict["Booklist"].append(row[0] + ", written by" + row[2] + ", published in" + str(published))
                books_dict["Count"] += 1

    return books_dict

def print_books_in_range(books_dict):
    '''find_books_in_range(startyear, endyear) will print out error message or display
    all books whose publication year is within the given inclusive range. Each line will
    contain the title of the book, the author, and the publication date.'''
    if "Error" in books_dict:
        print("You\'ve inputed an invalid year range. ENDYEAR needs to be later than STARTYEAR")
    else:
        if books_dict["Count"] == 0:
            print("We couldn't find any books that were published in between the date range")
        else:
            for book in books_dict["Booklist"]:
                print(book)

def get_parsed_arguments():
	'''Parsing command line interface and return all parsed_arguments'''
	parser = argparse.ArgumentParser(description='Process some books information')
	parser.add_argument('--author', '-a', help='Input key that you want to search upon for authors names', type=str)
	parser.add_argument('--title', '-t', help='Input key that you want to search upon for book titles', type=str)
	parser.add_argument('--daterange', '-d', nargs=2, metavar='YEAR', help='Input the year range that you want the book\'s publication year in', type=int)
	parsed_arguments = parser.parse_args()

	return parsed_arguments

def main():
	parsed_args = get_parsed_arguments()

    #depending on the command, run the proper functions
	if parsed_args.author:
		print_authors(search_authors(parsed_args.author))
	elif parsed_args.title:
		print_titles(search_titles(parsed_args.title))
	elif parsed_args.daterange:
		print_books_in_range(find_books_in_range(parsed_args.daterange[0], parsed_args.daterange[1]))
	else:
		print("Please enter a valid command option or -h/--help for help")

if __name__ == "__main__":
    main()
