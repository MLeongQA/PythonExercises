#code that can take in a sentence, break it down into its individual words,
#cut out any repeating words to only 1 and
#then print them in alphabetical order


def NoRepeatSort(sentence):
    example_set = set((sentence.lower()).split())
    print(sorted(example_set))


NoRepeatSort("This is an example sentence")
NoRepeatSort("This is an example sentence with a repeat. This is an example")
