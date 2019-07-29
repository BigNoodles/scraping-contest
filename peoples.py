#!/usr/bin/env python3

"""
Tries to determine a common category for famous people 
based on their Wikipedia categories.

Expects to find html files in local subdirectory "celebrities'
"""

#imports
from bs4 import BeautifulSoup
import collections
import os
import numpy as np
import matplotlib.pyplot as plt

#constants
PATH = os.getcwd() + '/celebrities/'
TOP = 5 #how many categories to consider the "top"


#functions
def get_soup(path):
    """
    Tries to open a local html file and return parsed soup or None.

    Input: filename string
    Output: BeautifulSoup tree
    """

    for celebrity in os.listdir(path):
        print(f'Trying to parse {celebrity[:-5]} ...')
        try:
            soup = BeautifulSoup(open(path + celebrity),'html.parser')
            yield soup

        except Exception as e:
            print(f'Could not open {celebrity}: {e}')
            yield None



def find_categories(all_soup):
    """
    Parses soup in search of Wikipedia categories

    Input: BeautifulSoup tree
    Output: collections.Counter of common categories
    """

    all_celebs = collections.Counter()

    #words we don't care about
    boring = ['categories','births','from','of','the','people']

    for soup in all_soup:
        #find div container for normal (not hidden) categories
        cat_div = soup.find('div',{'id':'mw-normal-catlinks'})
        #break out individual links
        cat_anchs = cat_div.find_all('a')
        c = collections.Counter()

        for category in cat_anchs:
            cat_clean = category.text.strip().lower()
            #split into individual words and update the Counter
            for word in cat_clean.split():
                if word not in boring:
                    c.update([word])
    
        #append this celebrity to the superset
        all_celebs = all_celebs + c

    return all_celebs



def pretty_output(all_celebs):
    """
    Prints information learned about the celebrities.

    Input: collections.Counter superset of categories 
    """

    top_cats = all_celebs.most_common(TOP)

    print(f'\nMost common categories for these celebrities:')
    for category, count in top_cats:
        print(f'{category}: {count} times')

    cats, counts = zip(*top_cats)

    plt.bar(cats, counts)
    plt.xlabel('Categories', fontsize=5)
    plt.ylabel('Frequency', fontsize=5)
    plt.title('Most common categories for these celebrities')
    plt.show()



def main():

    all_soup = get_soup(PATH)
    all_celebs = find_categories(all_soup)
    pretty_output(all_celebs)

    print(f'\nDone.')


if __name__ == '__main__':
    main()




