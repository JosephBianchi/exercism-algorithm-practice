# def is_isogram(string):
#     string = string.lower()
#     array = list(string)
#     check_array = []
#
#     for char in array:
#         if char != ' ' or char != '-':
#             if char in check_array:
#                 print(check_array)
#                 return False
#             else:
#                 check_array.append(char)
#         else:
#             check_array.append(char)
#     return True
#
#
#
#
# print(is_isogram("Emily Jung Schwartzkopf"))


def is_isogram(word):
    word = word.lower().replace(' ', '').replace('-', '')

    if len(word) == len(set(word)):
        return True
    else:
        return False
