def get_word_count(filename):

    word_count = {}

    with open(filename) as paragraph:
        for line in paragraph:
            line = line.rstrip()
            words = line.split(" ")
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    return word_count


for word, num in get_word_count('test.txt').items():
    print "{} {}".format(word, num)

for word, num in get_word_count('twain.txt').iteritems():
    print "{} {}".format(word, num)

