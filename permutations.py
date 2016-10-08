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

def unit_test():
    unit_test_num_permutations()
    return "unit_tests pass"

def unit_test_num_permutations():
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

if __name__ == "__main__":
    print(unit_test())
