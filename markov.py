"""Generate Markov text from text files."""

import random
import pprint
import sys



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    words = contents.split()
    return words


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    declare the empty dictionary

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    i = 0
    i1 = 1
    i2 = 2
    
    # your code goes here
    # while i1 < len(text_string) - 1:
    #     update_tuple = (text_string[i], text_string[i1])
    #     chains[update_tuple] = chains.get(update_tuple, [])
    #     chains[update_tuple].append(text_string[i2])
    #     i += 1
    #     i1 += 1
    #     i2 += 1

    while n < len(text_string) - 1:
        update_tuple = tuple(text_string[i:n])
        chains[update_tuple] = chains.get(update_tuple, [])
        chains[update_tuple].append(text_string[n + 1])
        i += 1
        i1 += 1
        n += 1
   
    return chains

# test_file = open_and_read_file("green-eggs.txt")
# pp=pprint.PrettyPrinter(indent=4)
# pp.pprint(make_chains(test_file))

def make_text(chains):
    """Return text from chains."""
    n = len(list(chains.keys())[0])
    words = []
    first_link = random.choice(list(chains.keys()))
    
    # words.append(first_link[0])
    # words.append(first_link[1])
    #print(words)
    i = 0

   
    # your code goes here
    # while i2 < len(words):
    #     update_tuple = (words[i1], words[i2])
    #     if update_tuple in chains.keys():
    #         new_link = random.choice(chains[update_tuple])
    #         i1 += 1
    #         i2 += 1
    #         words.append(new_link)
    #         #print(new_link)
    #     else:
    #         break
    for item in first_link:
        words.append(item)
    # n2 = n + 2

    while i < len(words) - 1:
        update_tuple = tuple(words[i:n])
        # print(update_tuple)

        if update_tuple in chains.keys():
            new_link = random.choice(chains[update_tuple]) 
            i += 1
            n += 1
            words.append(new_link)
            #print(new_link)
        else:
            break

    
    return ' '.join(words)


#input_path = 'green-eggs.txt'
#input_path ='gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text, 3)

# Produce random text
random_text = make_text(chains)

print(random_text)
