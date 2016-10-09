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

if __name__ == "__main__":
    from test_permutations import unit_test
    print(unit_test())
