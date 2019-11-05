import random
import sys

def get_file_lines(filename):
    lines = []
    file = open(filename, 'r')
    lines = file.readlines()
    clean_lines = [line.strip() for line in lines]
    file.close() 
    return clean_lines

def pick_random_word(word_list):
    index = random.randint(0, len(word_list) - 1)
    return word_list[index]

def sentence(num_words):
    random_words = []
    words = get_file_lines("/usr/share/dict/words")
    for i in range(num_words):
        random_words.append(pick_random_word(words))
    print(" ".join(random_words))
    
if __name__ == "__main__":
    num_words = sys.argv[1]
    num_words = int(num_words)
    sentence(num_words)