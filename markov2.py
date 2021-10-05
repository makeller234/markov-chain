"""Generate Markov text from text files."""

import random
import string
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
    #i1 = 1
    
    while i < len(text_string) - n:
        update_tuple = tuple(text_string[i:i+n])
        chains[update_tuple] = chains.get(update_tuple, [])
        chains[update_tuple].append(text_string[n + i])
        i += 1
        #i1 += 1
        #n += 1
    print(chains)
    return chains

def make_text(chains):
    """Return text from chains."""
    n = len(list(chains.keys())[0])
    punc = ['?', '.', '!']
    words = []
    first_link = random.choice(list(chains.keys()))
    while first_link[0][0].isupper() != True:
        first_link = random.choice(list(chains.keys()))
        
    i = 0

    for item in first_link:
        words.append(item)
    # print(f'before: {words[-1][-1]}')
    while words[-1][-1] not in punc:
        update_tuple = tuple(words[i:n])

        if update_tuple in chains.keys():
            new_link = random.choice(chains[update_tuple]) 
            i += 1
            n += 1
            words.append(new_link)
            #print(f'after: {words[-1][-1]}')
        #elif words[-1][-1] in punc:

        # else:
        #     break
    
    return ' '.join(words)



# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text, 3)

# Produce random text
random_text = make_text(chains)

print(random_text)
