from permutations import num_permutations, rank, permute, ith_permutation
from collections import Counter
from math import factorial
from functools import reduce
import itertools

def unit_test():
    unit_test_num_permutations()
    unit_test_rank()
    unit_test_permutations()
    unit_test_ith_permutation()
    return "unit_tests pass"

def unit_test_num_permutations():
    for word in '', 'a', 'aa', 'aaa':
        assert num_permutations(word) == 1
    for word in 'ab', 'ba', 'cb', 'xy':
        assert num_permutations(word) == 2

    for word in 'abc', 'abcdef', 'xyab', 'xyabzeoijk':
        assert num_permutations(word) == factorial(len(word))

    for word in 'aababab', 'aba', 'acejadfjdjafj', 'jfkskdfjdkkjjjj':
        perms = reduce(lambda total, count: total / factorial(count),
                       Counter(word).values(),
                       factorial(len(word)))
        assert num_permutations(word) == perms

def unit_test_rank():
    for i, word in enumerate(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']):
        assert rank(word) == i
    for i, word in enumerate(sorted(set(itertools.permutations('aabc')))):
        assert rank(word) == i
    for i, word in enumerate(sorted(set(itertools.permutations('abbbdjdc')))):
        assert rank(word) == i

def unit_test_permutations():
    assert sorted(permute('j')) == ['j']
    assert sorted(permute('dog')) == sorted(['dog', 'dgo', 'odg', 'ogd', 'god', 'gdo'])
    assert sorted(permute('aabc')) == sorted([
        'aabc', 'aacb', 'abac', 'abca', 'acab', 'acba', 
        'baac', 'baca', 'bcaa', 'caab', 'caba', 'cbaa'])
    assert [w for w in permute('bac')] == ['bac', 'bca', 'abc', 'acb', 'cba', 'cab']

def unit_test_ith_permutation():
    assert ith_permutation(0, 'abc') == 'abc'
    assert ith_permutation(0, 'bac') == 'abc'
    assert ith_permutation(0, 'cba') == 'abc'
    assert ith_permutation(1, 'bac') == 'acb'
    for i, permutation in enumerate(permute('abc')):
        assert ith_permutation(i, 'cba') == permutation
    assert ith_permutation(0, 'abac') == 'aabc'
    assert ith_permutation(1, 'abac') == 'aacb'
    assert ith_permutation(6, 'abac') == 'baac'
    assert ith_permutation(11, 'abac') == 'cbaa'
    assert ith_permutation(12, 'abac') == 'aabc'


