'''
  booksdatasourcetests.py
  Alison Cameron and Cathy Guang
  CS257 Fall 2020
'''
import booksdatasource
import unittest


class BooksDataSourceTester(unittest.TestCase):
  def setUp(self):
    self.bds = booksdatasource.BooksDataSource('bookstest.csv', 'authorstest.csv')

  def tearDown(self):
    pass

  def test_booksf_author_id_exists(self):
    return_list = [{'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}]
    self.assertEqual(self.bds.books(author_id=22), return_list)

  def test_booksf_author_id_empty(self):
    with self.assertRaises(ValueError):
      self.bds.books(author_id=13)
  
  def test_booksf_search_text_exists(self):
    return_list = [{'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}]
    self.assertEqual(self.bds.books(search_text='Great Exp'), return_list)

  def test_booksf_search_text_empty(self):
    return_list = []
    self.assertEqual(self.bds.books(search_text='Moby Dick'), return_list)

  def test_booksf_start_year(self):
    book = {'title': 'All Clear', 'publication_year': 2010, 'author_id': 0}
    self.assertIn(book, self.bds.books(start_year=2000))

  def test_booksf_end_year(self):
    book = {'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}
    self.assertIn(book, self.bds.books(end_year=2000))

  def test_booksf_sort_by_title(self):
    return_list = [{'title': 'All Clear', 'publication_year': 2010, 'author_id': 0},
    {'title': 'Blackout', 'publication_year': 2010, 'author_id': 0}, {'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}, {'title': 'Middlemarch', 'publication_year': 1871, 'author_id': 21}]
    self.assertEqual(self.bds.books(sort_by='title'), return_list)

  def test_booksf_sort_by_pub_year(self):
    return_list = [{'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}, {'title': 'Middlemarch', 'publication_year': 1871, 'author_id': 21}, {'title': 'All Clear', 'publication_year': 2010, 'author_id': 0},
    {'title': 'Blackout', 'publication_year': 2010, 'author_id': 0}]
    self.assertEqual(self.bds.books(sort_by='year'), return_list)

  def test_booksf_year_range(self):
    book = {'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}
    self.assertIn(book, self.bds.books(start_year=1700, end_year=2000))

  def test_booksf_author_id_search_text(self):
    return_list = [{'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}]
    self.assertEqual(self.bds.books(author_id=22, search_text='grea'), return_list)

  def test_booksf_author_id_start_year(self):
    return_list = [{'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}]
    self.assertEqual(self.bds.books(author_id=22, start_year=1860), return_list)

  def test_booksf_author_id_year_range(self):
    return_list = [{'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}]
    self.assertEqual(self.bds.books(author_id=22, start_year=1850, end_year=1870), return_list)

  def test_booksf_search_text_sort_by_pub_year(self):
    return_list = [{'title': 'Great Expectations', 'publication_year': 1860, 'author_id': 22}, {'title': 'All Clear', 'publication_year': 2010, 'author_id': 0}]
    self.assertEqual(self.bds.books(search_text='ea', sort_by='year'), return_list)

  def test_booksf_author_id_invalid(self):
    '''This method raises a ValueError if author_id is non-None but is not a valid author ID.
	'''
    with self.assertRaises(ValueError):
      self.bds.books(author_id='13')

  def test_booksf_year_range_invalid(self):
    '''Testing cases where start_year > end_year'''
    return_list = []
    self.assertEqual(self.bds.books(start_year=1870, end_year=1860), return_list)

  def test_authorf_search_text_exists(self):
    author = {'id': 22, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': 1812, 'death_year': '1870'}
    self.assertIn(author, self.bds.authors(search_text='Char'))

  def test_authorf_search_text_empty(self):
    return_list = []
    self.assertEqual(self.bds.authors(search_text='George'), return_list)

  def test_authorf_search_text_none(self):
    return_list = [{'id': 4, 'last_name': 'Austen', 'first_name': 'Jane', 'birth_year': 1775, 'death_year': '1817'}, {'id': 22, 'last_name': 'Dickens', 'first_name': 'Charles', 'birth_year': 1812, 'death_year': '1870'}, {'id': 2, 'last_name': 'Morrison', 'first_name': 'Toni', 'birth_year': 1931, 'death_year': None}]
    self.assertEqual(self.bds.authors(), return_list)

if __name__ == '__main__':
    unittest.main()