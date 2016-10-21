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

def ith_permutation(i, word):
    """Find the i-th lexographic permutation of a word."""
    permutations = num_permutations(word)
    counts = Counter(word)
    ordered = sorted(counts.keys())
    len_word = len(word)
    rotations_remaining = i % permutations
    built_permutation = []

    def permutations_without_char(len_word, char):
        return permutations * counts[char] / len_word

    while rotations_remaining:
        for char in ordered:
            perms_without_char = permutations_without_char(len_word, char)
            if rotations_remaining and perms_without_char <= rotations_remaining:
                rotations_remaining -= perms_without_char
            else:
                built_permutation.append(char)
                permutations = perms_without_char
                len_word -= 1
                counts[char] -= 1
                if not counts[char]:
                    ordered.pop(ordered.index(char))
                break
    built_permutation.append(''.join(sorted(counts.elements())))
    return ''.join(built_permutation)


def permute(word):
    """Create an iterator with all permutations of given word."""
    if len(word) <= 1:
        return [word]

    leader_indices, used = [], set()
    for i, char in enumerate(word):
        if char not in used:
            leader_indices.append(i)
            used.add(char)
            
    return (word[i] + suffix for i in leader_indices
            for suffix in permute(word[:i] + word[i+1:]))

def next_permutation(word):
    """Return the next lexographic permutation of a word."""
    # 1. find first char not ascending
    word = list(word)
    i = len(word) - 1
    while i > 0 and word[i - 1] >= word[i]:
        i -= 1
    if i > 0:
        j = len(word) - 1
        while word[j] <= word[i - 1]:
            j -= 1
        word[i - 1], word[j] = word[j], word[i - 1]
    return ''.join(word[:i] + word[i:][::-1])


if __name__ == "__main__":
    from test_permutations import unit_test
    print(unit_test())
