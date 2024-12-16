words= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

def find_long_words(words, n):
    long_words = []
    for word in words:
        if len(word) > n:
            long_words.append(word)
    return long_words

print(find_long_words(words,4))