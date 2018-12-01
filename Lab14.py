# Sara Kazemi
# Lab 14 - CST 205
# Create a count of how many total distinct words appear in Green Eggs and Ham
# Create a count of how often each of the words appears
# Print out the total distinct count and the count for each of the words.
# Print out the most commonly occurring word in the book

original_text = open('eggs.txt', 'r')

# Returns total word count found in the text
def word_count(text):
    count = 0
    for line in text:
        line = line.strip().split()  # strip of leading/trailing whitespace and put each word in list
        count += len(line)  # word count is simply the length of each list since elements are words found in line
    return count

# Finds all unique words in the text and adds them to the dictionary keys
# If found again, increments the count held in the key's corresponding value.
def get_unique_words(text):
    unique_words = {}
    for line in text:
        line = line.strip().lower().split()
        for word in line:
            if word not in unique_words:
                unique_words.update({word: 1})
            else:
                unique_words[word] = unique_words[word] + 1
    return unique_words

# Length of the dictionary is equivalent to the number of unique word in text
def unique_word_count(dict):
    return len(dict)

# Prints out unique words from the text in unsorted order
# with their counts.
def print_dictionary(dict):
    for key in dict:
        print(f'word: {key:10} | count: {dict[key]:10}')

# Prints out unique words from the text in alphabetical order
# with their counts.
def print_dict_alpha(dict):
    sorted_dict = sorted(dict)
    for word in sorted_dict:
        print(f'word: {word:10} | count: {dict[word]:10}')

# Find the larges value in the dictionary to get most frequent word
def get_most_frequent(dict):
    values=[]
    for value in dict.values():
        values.append(value)
    return max(values)

# Print out the most frequent word and its count
def get_most_freq_word(max, dict):
    for word in dict:
        if dict[word] == max:
            print(f'\t*****MOST FREQUENT WORD*****\nword: {word:10} | count: {dict[word]:10}')


def main():
    dictionary = get_unique_words(original_text)
    print_dict_alpha(dictionary)
    max = get_most_frequent(dictionary)
    get_most_freq_word(max, dictionary)
    print(f'\t\t*********************\nUnique word count: {unique_word_count(dictionary): 17}')

main()



