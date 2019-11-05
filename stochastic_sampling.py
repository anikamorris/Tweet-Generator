from histogram import list_of_lists_histogram, file_or_string
import random
import sys

def get_total_weight(histogram):
    '''Finds total number of words in a given histogram
    PARAMETERS:
    histogram: list of lists'''
    total_weight = 0
    for item in histogram:
        total_weight += item[1]
    return total_weight

def random_weighted_word(histogram):
    '''Uses get_total_weight helper function to get a random word 
    from the histogram at the same frequency at which each word appears
    PARAMETERS:
    histogram: list of lists'''
    total_weight = get_total_weight(histogram)
    random_weight = random.randint(0, total_weight)
    for item in histogram:
        random_weight = random_weight - item[1]
        if random_weight <= 0:
            return item[0]

def get_sentence(histogram, amount=15):
    '''Uses the random_weighted_word function to get weighted words and
    combine them in a sentence
    PARAMETERS:
    histogram: list of lists
    amount: int (default = 15 words)'''
    words = []
    for i in range(amount):
        words.append(random_weighted_word(histogram))
    sentence = ' '.join(words)
    return sentence


if __name__ == "__main__":
    entry = f"../Code/{sys.argv[1]}"
    histogram = list_of_lists_histogram(entry)
    print(get_sentence(histogram, 30))
