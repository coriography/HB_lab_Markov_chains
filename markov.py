"""Generate Markov text from text files."""

import random
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # open file_path, save to a variable
    # use read method

    file_contents = open(file_path).read()

    return file_contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

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
    # Replace text string line breaks with a space
    # Assign split text string by the spaces to variable words = text_string.split()
    # Loop through words and send each pair of words to chains as as key
        #Find the words that come after that pair and add to a list of values that go to that pair

    words = text_string.rstrip().split()
    chains = {}

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)    

    return chains


def make_text(chains):
    """Return text from chains."""
    
    # pick random key 
    # put chosen key into words list
    # pick random value of key
    # rand_value = chains[rand_key]
        # loop through values of our chosen key
    # add random value to words list
    # assign last two words to variable, last_words = words[-2:] - this gives us new key
    # then select new rand_value
    # repeat until last two items in words list are not key in chains

    words = []
    
    key_list = sorted(chains)
    print(f' this is our key list: {key_list}')

    rand_key = random.choice(key_list)
    print(f' this is rand_key {rand_key}')

    words.append(rand_key)
    print(f'this is words {words}')

    values = chains[rand_key]
    print(f'this is values {values}')

    rand_value = random.choice(values)
    print(f'this is rand_value {rand_value}')

    words.append(rand_value)
    print(f'this is words {words}')

    last_words = words[-2:]

    # if last_words in chains:
        # create new key with new last two words
        # get random value
        # append new value


    # print(words)
    # return words
    # return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
