paragraph = open("twain.txt")
word_count = {}


for line in paragraph:
    line = line.rstrip()
    words = line.split(" ")
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

print word_count


# cohort = open('cohort_data.txt')
#     for line in cohort:
#         student = line.split('|')
#         houses.add(student[2])