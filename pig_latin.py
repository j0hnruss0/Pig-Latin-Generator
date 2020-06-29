"""Change a whole sentence into pig latin!"""
import sys
import re

VOWELS = "aeiouy"
# more entries to be added to DO_NOT_CHANGE to be added if needed
DO_NOT_CHANGE = ["on", "the", "a", "an", "if", "and", "are"]
punc_list = ["?", "!", "."]

while True:
    sentence = input("Enter a sentence to convert to pig latin:\n")
    punc_output = []
    if sentence[-1] in punc_list:
        punc_output.append(sentence[-1])
    sentence_fix = re.sub(r'[^\w\s]','',sentence)
    words = sentence_fix.split()
    output = []
    for word in words:
        if word not in DO_NOT_CHANGE:
            if word[0] in VOWELS:
                new_word = word + 'way'
                output.append(new_word)
            else:
                new_word = word[1: ] + word[0] + "ay"
                output.append(new_word)
        else:
            output.append(word)
    NEW_SENTANCE = " ".join(output)
    print()
    print("{}{}".format(NEW_SENTANCE, "".join(punc_output)), file=sys.stderr)

    try_again = input("\n\nWant to try a new sentance? (Press Enter else 'n' to stop)\n")
    if try_again.lower() == "n":
        sys.exit()
