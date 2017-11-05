def word_count(phrase):
    words = phrase.lower().split()
    check_list = {}
    for word in words:
        if word not in check_list:
            check_list[word] = 1
        else:
            check_list[word] += 1
    return check_list


print(word_count('one,two,three'))
