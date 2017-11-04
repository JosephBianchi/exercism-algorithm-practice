import re


def is_pangram(sentence):
    string = sentence.lower()
    string = re.sub('[^a-zA-Z]+', '', string)
    print(string)
    if len(set(string)) == 26:
        print (set(string))
        print(len(set(string)))
        return True
    else:
        print (set(string))
        print(len(set(string)))
        return False

is_pangram('the 1 quick brown fox jumps over the 2 lazy dogs')
