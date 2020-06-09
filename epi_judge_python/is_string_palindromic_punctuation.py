from test_framework import generic_test

# # Strip punctuation and whitespaces
# # Not space efficient
# def is_palindrome(s: str) -> bool:
#     # TODO - you fill in here.
#     s = s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
#     return all(s[i]==s[~i] for i in range(len(s)//2))

# # O(1) solution - 2 pointer approach
# def is_palindrome_O1(s: str) -> bool:
#     i, j = 0, len(s) -1
#     while (i < j):
#         while not s[i].isalnum() and i < j:
#             i += 1
#         while not s[j].isalnum() and i < j:
#             j -=1
#         if s[i].lower() == s[j].lower():
#             i, j = i+1, j-1
#         else:
#             return False
#     return True

# filter(str.isalnum, s) returns alphanumeric characters
def is_palindrome(s):
    return all(
        a == b
        for a, b in zip(map(str.lower, filter(str.isalnum, s)),
                        map(str.lower, filter(str.isalnum, reversed(s)))))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
