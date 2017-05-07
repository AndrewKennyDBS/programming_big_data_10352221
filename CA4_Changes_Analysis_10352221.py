#CA4_Changes_Analysis
#Student Number: 10352221
#github: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

import operator

def read_file(changes_file):                                                        # Reads file
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):                                                              # Parses commits places them into relevant container objects
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    
    while index < len(data):
        try:
            details = data[index + 1].split('|')

            commit = {'Revision': details[0].strip(),                           
                      'Author': details[1].strip(),                             
                      'Date': details[2].strip(),
                      'Line Count': details[3].strip(),
                      'Changes': data[index+2:data.index('',index+1)],
            }
            
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

def get_authors(commits):                                                       # Finds occurences of author name in list of commits
    authors = {}
    
    for commit in commits:
        author = commit['Author']
        if author not in authors:
            authors[author] = 1
        else:
            authors[author] = authors[author] + 1
    return authors
    
def sort_authors(authors):
    return sorted(authors.items(), key=operator.itemgetter(1))                  # Sorts number of commits by author
    
if __name__ == '__main__':
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
    authors = get_authors(commits)
    sorted_author = sort_authors(authors)

    print "Lines in document: ",(len(data))                                     # Prints number of lines in document
    print "Number of commits: ",(len(commits))                                  # 1. Total number of commits
    print "Number of authors: ",(len(authors))                                  # 2. Total number of authors
    print "Commits by author: ",(sorted_author)                                 # 3. Commits made by author, lowest to highest