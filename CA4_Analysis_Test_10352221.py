#CA4_Analysis_Test
#Student Number: 10352221
#github: https://github.com/AndrewKennyDBS/programming_big_data_10352221.git

import unittest

from CA4_Changes_Analysis_10352221 import read_file, get_commits, get_authors, sort_authors

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):                                             #Test no of lines in document is = 5255
        self.assertEqual(5255, len(self.data))
        
    def test_first_commit(self):                                                #Testing first commit details are correct
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['Author'])
        self.assertEqual('r1551925', commits[0]['Revision'])

    def test_number_of_commits(self):                                           #Test no of commits is = 422
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_number_of_authors(self):                                           #Test no of authors is = 10
        commits = get_commits(self.data)
        authors = get_authors(commits)
        print (len(authors))
        
        self.assertEqual(10, len(authors))

    def test_commits_by_authors(self):                                          #Test no of commits by author
        commits = get_commits(self.data)
        authors = get_authors(commits)
        sorted_authors = sort_authors(authors)
        sorted_authors.reverse()
        print sorted_authors
        
        self.assertEqual(191, authors['Thomas'])

if __name__ == '__main__':
    unittest.main()