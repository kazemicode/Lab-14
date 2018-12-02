# Sara Kazemi
# Lab 14 - CST 205

# Problem 1
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

# Problem 2
# Extract headlines from the news web page https://foothill.edu/news/

source_html = open('source.html', 'r').read()

# Finds each featured headline in Foothill's website by getting
# the substring that occurs between h3 html tags and appending those
# substrings to a list.
def find_news(source):
    doc=source
    goal_start="&lt;h3&gt;</span>" # Title of each featured headline is preceded by an h3 HTML tag
    goal_end="<span class=\"html-tag\">&lt;/h3&gt;</span>" # Title of each featured headline is followed by
                                                           # a closing h3 tag
    psn = doc.find(goal_start, 0)  # position starts at first instance of an h3 tag in the document string
    headlines=[] # initialize list of found headlines
    while doc.find(goal_start, psn) > -1: # as long as we still find h3 tags in our doc, keep searching
        psn = doc.find(goal_start, psn)   # psn reassigned to the position of the next h3 tag found
        start = psn + len(goal_start)     # start of our headline is just after the end of the h3 tag
        end = doc.find(goal_end, start)   # end of our headline is right before the closing h3 tag
        headlines.append(doc[start:end])  # append the headline to the list
        psn = start                       # reassign psn to just after the last h3 tag we found ends

    return headlines

# Prints each headline in the list
def print_headlines(headline_list):
    print("LIST OF HEADLINES:\n")
    for headline in headline_list:
        print(headline)


def main():
    print("\n\nProblem 1:\n")
    dictionary = get_unique_words(original_text)
    print_dict_alpha(dictionary)
    max = get_most_frequent(dictionary)
    get_most_freq_word(max, dictionary)
    print(f'\t\t*********************\nUnique word count: {unique_word_count(dictionary): 17}')
    headlines = find_news(source_html)
    print("\n\n\t\t*********************\n\nProblem 2:\n")
    print_headlines(headlines)


main()


