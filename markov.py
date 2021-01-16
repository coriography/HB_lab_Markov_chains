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

    sentence = []
    key_list = sorted(chains)

    # pick random key 
    current_key = random.choice(key_list)

    # put chosen key into sentence list
    sentence.extend(current_key)

    # repeat until last two items in sentence list are not a key in chains:
    while current_key in chains: 

        # select random value of key
        # values = chains[current_key]
        rand_value = random.choice(chains[current_key])

        # add random value to sentence list
        sentence.append(rand_value)

        # assign last two sentence to variable this gives us new key
        current_key = tuple(sentence[-2:])
        
    return ' '.join(sentence)


# Hackbright's solution:
# def make_text(chains):
#     """Return text from chains."""

#     key = choice(list(chains.keys()))
#     words = [key[0], key[1]]
#     word = choice(chains[key])

#     # Keep looping until we reach a value of None
#     # (which would mean it was the end of our original text)
#     # Note that for long texts (like a full book), this might mean
#     # it would run for a very long time.

#     while word is not None:
#         key = (key[1], word)
#         words.append(word)
#         word = choice(chains[key])

#     return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
