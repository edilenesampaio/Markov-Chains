"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    string = open("green-eggs.txt").read()
    

    return string


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

    chains = {}

    list_of_words = text_string.split()

    word_list =[]

    for i in range(len(list_of_words)-2): 
        tuple_of_list = (list_of_words[i],list_of_words[i+1])
        value_of_list = list_of_words[i+2]

        if tuple_of_list not in chains: 
            chains[tuple_of_list] = [value_of_list]

        else:
            chains[tuple_of_list].append(value_of_list)


    return chains


def make_text(chains):
    """Return text from chains."""

    # print(chains)

    #make a list of all the keys we have with the .keys() function
    # keys = choice(word_list)
    key_list= []

    for chain in chains.keys():
        key_list.append(chain)

    # print("this is key_list")
    # print(key_list)
    

    #randomly select from this list of keys we've accessed 
    # random_chain = choice(list(new_chains))

    random_chain = choice(key_list)
    # print("This is random_chain:")
    # print(random_chain)
 
    #randomly select a value from list of words associated with the key
    random_value = choice(chains[random_chain])
    # print(random_value) 

    #once we have our key (tuple) and word pair, we can add them both to a list
    words = []

    words.append(random_chain[0])
    words.append(random_chain[1])
    # print(words)
    words.append(random_value)
    print(words)
    
 
    #use the second word of the key pair plus the same random word from above
    #negative indexing to access the last two 
    

    new_key_lookup = []

    new_key_lookup.append(words[-2])
    new_key_lookup.append(words[-1])
    

    print(new_key_lookup)

    # print(chain[new_key_lookup])
    # while 

    #look this second key + random value up in the dictionary

    #you need the first three words before establishing the while loop

    #add to list above

    #repeat until we get a key error
    



    # return ' '.join(words) #uncomment this at the end after resolving other lines


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)


#various test code

# print(open_and_read_file("green-eggs.txt"))

# print(make_chains(open_and_read_file("green-eggs.txt")))

# print(make_text("green-eggs.txt"))
