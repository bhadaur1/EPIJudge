from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.
    if not L:
        return True
    curr = L
    vals = [curr.data]
    while (curr.next):
        curr = curr.next
        vals.append(curr.data)
    return all(vals[i] == vals[~i] for i in range(len(vals)//2))

    # return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
