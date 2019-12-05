from dictogram import Dictogram
import random

def higher_order(word_list, new_words, order=2):
    """
    Parameters:
    word_list: List
    new_words: String
    order: Int

    Returns:
    storage_dict: dict where key is new_words and value is a Dictogram
    """
    storage_dict = dict()

    key_words = new_words.split()
    if len(key_words) != order:
        return "Length of input words does not equal order"

    words = []
    next_words = []
    next_pairs = []

    for i in range(len(word_list) - 1):
        words.clear()
        for j in range(order):
            words.append(word_list[i + j])
        if key_words == words:
            next_words.clear()
            for j in range(order):
                next_words.append(word_list[i + (j + 1)])
            next_words_str = " ".join(next_words)
            next_pairs.append(next_words_str)

    storage_dict[new_words] = Dictogram(next_pairs)
    return storage_dict

def new_chain(word_list, word):
    """If word is in word_list, append the next word to a list.
       Then create a new histogram with the list of following words.
       
       Parameters:
       word_list: List
       word: String

       Returns:
       chain: Dictogram
    """
    chain_list = []
    for i in range(len(word_list) - 1):
        if word == word_list[i]:
            chain_list.append(word_list[i + 1])

    chain = Dictogram(chain_list)
    return chain

def walk(word_list, length):
    """Start sentence with sample word from full histogram. 
       Sample each new histogram chain to get next word, add to sentence. 
       
       Parameters:
       word_list: List
       length: Int

       Returns:
       sentence: List
    """
    sentence = []
    histogram = Dictogram(word_list)
    next_word = histogram.sample()
    sentence.append(next_word)
    for i in range(length - 1):
        chain = new_chain(word_list, next_word)
        if len(chain) > 0:
            next_word = chain.sample()
            sentence.append(next_word)

    return sentence

def create_sentence(words):
    """Joins words in a list, capitalizes the first word and adds a period to the end. 

        Parameters:
        words: List

        Returns:
        formatted_sentence: String
    """
    words[0] = words[0].capitalize()
    formatted_sentence = ' '.join(words) + '.'

    return formatted_sentence

if __name__ == "__main__":
    word_list = ['one', 'fish', 'two', 'fish', 'two', 'fish', 'blue', 'fish', 'cat']
    # print(create_sentence(walk(word_list, 15)))
    print(higher_order(word_list, "fish two", 3))