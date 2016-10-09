"""Various helper methods for working with permutations."""
from collections import Counter

def num_permutations(word):
    """Return the number of permutations possible given a word."""
    counts = Counter()
    permutations = 1
    for i, char in enumerate(word):
        counts[char] += 1
        permutations = permutations * (i + 1) / counts[char]
    return permutations

def rank(word):
    """Get the lexicographic order of a word relative to all of its permutations."""
    counts = Counter(word)
    ordered = sorted(counts.keys())
    permutations = num_permutations(word)
    num_before = 0

    def permutations_without_char(len_word, char):
        return permutations * counts[char] / len_word

    for i, char in enumerate(word):
        ordered_chars = iter(ordered)
        cur = ordered_chars.next()
        while cur != char:
            num_before += permutations_without_char(len(word) - i, cur)
            cur = ordered_chars.next()
        permutations = permutations_without_char(len(word) - i, char)
        counts[char] -= 1
        if not counts[char]:
            ordered.remove(char)
    return num_before


def __unit_test():
    __unit_test_num_permutations()
    __unit_test_rank()
    return "unit_tests pass"

def __unit_test_num_permutations():
    for word in '', 'a', 'aa', 'aaa':
        assert num_permutations(word) == 1
    for word in 'ab', 'ba', 'cb', 'xy':
        assert num_permutations(word) == 2

    from math import factorial
    for word in 'abc', 'abcdef', 'xyab', 'xyabzeoijk':
        assert num_permutations(word) == factorial(len(word))

    from functools import reduce
    for word in 'aababab', 'aba', 'acejadfjdjafj', 'jfkskdfjdkkjjjj':
        perms = reduce(lambda total, count: total / factorial(count),
                       Counter(word).values(),
                       factorial(len(word)))
        assert num_permutations(word) == perms

def __unit_test_rank():
    for i, word in enumerate(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']):
        assert rank(word) == i


if __name__ == "__main__":
    print(__unit_test())
