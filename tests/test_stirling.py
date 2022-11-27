from collections import Counter
from itertools import product, chain

from pytest import mark, raises

from stirling import k_subsets
from stirling.stirling import s2


def test_n_0__k_0():
    assert list(k_subsets(set(), 0)) == [
        []  # One solution containing zero partitions
    ]

def test_n_0__k_1():
    assert list(k_subsets(set(), 1)) == []


def test_n_1__k_0():
    assert list(k_subsets([1], 0)) == []


def test_n_1__k_1():
    assert list(k_subsets([1], 1)) == [
        [[1]]
    ]


def test_n_2__k_1():
    assert list(k_subsets([1, 2], 1)) == [
        [[1, 2]]
    ]


def test_n_2__k_2():
    assert list(k_subsets([1, 2], 2)) == [
        [[1], [2]]
    ]

def test_n_2__k_3():
    assert list(k_subsets([1, 2], 3)) == [
    ]


def test_n_3__k_0():
    assert list(k_subsets([1, 2, 3], 0)) == [
    ]


def test_n_3__k_1():
    assert list(k_subsets([1, 2, 3], 1)) == [
        [[1, 2, 3]]
    ]


def test_n_3__k_2():
    assert list(k_subsets([1, 2, 3], 2)) == [
        [[1, 2], [3]],
        [[1, 3], [2]],
        [[1], [2, 3]],
    ]


def test_n_3__k_3():
    assert list(k_subsets([1, 2, 3], 3)) == [
        [[1], [2], [3]],
    ]


def test_n_4__k_0():
    assert list(k_subsets([1, 2, 3, 4], 0)) == [
    ]


def test_n_4__k_1():
    assert list(k_subsets([1, 2, 3, 4], 1)) == [
        [[1, 2, 3, 4]],
    ]


def test_n_4__k_2():
    assert list(k_subsets([1, 2, 3, 4], 2)) == [
         [[1, 2, 3], [4]],
         [[1, 2, 4], [3]],
         [[1, 2], [3, 4]],
         [[1, 3, 4], [2]],
         [[1, 3], [2, 4]],
         [[1, 4], [2, 3]],
         [[1], [2, 3, 4]],
    ]

def test_n_4__k_3():
    assert list(k_subsets([1, 2, 3, 4], 3)) == [
        [[1, 2], [3], [4]],
        [[1, 3], [2], [4]],
        [[1], [2, 3], [4]],
        [[1, 4], [2], [3]],
        [[1], [2, 4], [3]],
        [[1], [2], [3, 4]],
    ]

def test_n_4__k_4():
    assert list(k_subsets([1, 2, 3, 4], 4)) == [
        [[1], [2], [3], [4]],
    ]


def test_n_5__k_0():
    assert list(k_subsets([1, 2, 3, 4, 5], 0)) == []


def test_n_5__k_1():
    assert list(k_subsets([1, 2, 3, 4, 5], 1)) == [
        [[1, 2, 3, 4, 5]],
    ]

def test_n_5__k_2():
    assert list(k_subsets([1, 2, 3, 4, 5], 2)) == [
        [[1, 2, 3, 4], [5]],
        [[1, 2, 3, 5], [4]],
        [[1, 2, 3], [4, 5]],
        [[1, 2, 4, 5], [3]],
        [[1, 2, 4], [3, 5]],
        [[1, 2, 5], [3, 4]],
        [[1, 2], [3, 4, 5]],
        [[1, 3, 4, 5], [2]],
        [[1, 3, 4], [2, 5]],
        [[1, 3, 5], [2, 4]],
        [[1, 3], [2, 4, 5]],
        [[1, 4, 5], [2, 3]],
        [[1, 4], [2, 3, 5]],
        [[1, 5], [2, 3, 4]],
        [[1], [2, 3, 4, 5]]
    ]


def test_n_5__k_3():
    assert list(k_subsets([1, 2, 3, 4, 5], 3)) == [
        [[1, 2, 3], [4], [5]],
        [[1, 2, 4], [3], [5]],
        [[1, 2], [3, 4], [5]],
        [[1, 3, 4], [2], [5]],
        [[1, 3], [2, 4], [5]],
        [[1, 4], [2, 3], [5]],
        [[1], [2, 3, 4], [5]],
        [[1, 2, 5], [3], [4]],
        [[1, 2], [3, 5], [4]],
        [[1, 2], [3], [4, 5]],
        [[1, 3, 5], [2], [4]],
        [[1, 3], [2, 5], [4]],
        [[1, 3], [2], [4, 5]],
        [[1, 5], [2, 3], [4]],
        [[1], [2, 3, 5], [4]],
        [[1], [2, 3], [4, 5]],
        [[1, 4, 5], [2], [3]],
        [[1, 4], [2, 5], [3]],
        [[1, 4], [2], [3, 5]],
        [[1, 5], [2, 4], [3]],
        [[1], [2, 4, 5], [3]],
        [[1], [2, 4], [3, 5]],
        [[1, 5], [2], [3, 4]],
        [[1], [2, 5], [3, 4]],
        [[1], [2], [3, 4, 5]],
    ]

def test_n_5__k_4():
    assert list(k_subsets([1, 2, 3, 4, 5], 4)) == [
        [[1, 2], [3], [4], [5]],
        [[1, 3], [2], [4], [5]],
        [[1], [2, 3], [4], [5]],
        [[1, 4], [2], [3], [5]],
        [[1], [2, 4], [3], [5]],
        [[1], [2], [3, 4], [5]],
        [[1, 5], [2], [3], [4]],
        [[1], [2, 5], [3], [4]],
        [[1], [2], [3, 5], [4]],
        [[1], [2], [3], [4, 5]]
    ]


def test_n_5__k_5():
    assert list(k_subsets([1, 2, 3, 4, 5], 5)) == [
        [[1], [2], [3], [4], [5]],
    ]


def test_n_8_k_5():
    assert sum(1 for _ in k_subsets(list(range(8)), 5)) == 1050


@mark.parametrize(
    "n, k",
    product(range(11), range(11))
)
def test_number_of_arrangements_is_equal_to_stirling_number(n, k):
    s = list(range(n))
    count = sum(1 for _ in k_subsets(s, k))
    assert count == s2(n, k)


@mark.parametrize(
    "n, k",
    product(range(11), range(11))
)
def test_number_of_partitions_is_equal_to_k(n, k):
    s = list(range(n))
    assert all(len(arrangement) == k for arrangement in k_subsets(s, k))


@mark.parametrize(
    "n, k",
    product(range(11), range(11))
)
def test_partition_sizes_sum_to_n(n, k):
    s = list(range(n))
    assert all(sum(len(p) for p in arrangement) == n for arrangement in k_subsets(s, k))


@mark.parametrize(
    "n, k",
    product(range(11), range(11))
)
def test_partitions_are_disjoint(n, k):
    s = list(range(n))
    assert all(
        all(
            v == 1
            for v in Counter(chain.from_iterable(arrangement)).values()
        )
        for arrangement in k_subsets(s, k)
    )


@mark.parametrize(
    "n, k",
    product(range(11), range(11))
)
def test_all_original_items_are_represented(n, k):
    s = set(range(n))
    t = list(s)
    assert all(
        e in s
        for arrangement in k_subsets(t, k)
        for partition in arrangement
        for e in partition
    )

@mark.parametrize(
    "n, k",
    product(range(11), range(11))
)
def test_all_arrangements_are_distinct(n, k):
    s = list(range(n))
    assert all(
        v == 1
        for v in Counter(
            tuple(
                tuple(p)
                for p in arrangement
            )
            for arrangement in k_subsets(s, k)
        ).values()
    )


def test_k_subsets_with_negative_k_raises_value_error():
    with raises(ValueError):
        list(k_subsets([1, 2, 3], -1))


def test_s2_with_negative_n_raises_value_error():
    with raises(ValueError):
        s2(-1, 1)


def test_s2_with_negative_k_raises_value_error():
    with raises(ValueError):
        s2(5, -1)


@mark.parametrize(
    "n, k, s",
    [
        (
            n,
            k,
            [
                [1, 0],
                [0, 1, 0],
                [0, 1, 1, 0],
                [0, 1, 3, 1, 0],
                [0, 1, 7, 6, 1, 0],
                [0, 1, 15, 25, 10, 1, 0],
                [0, 1, 31, 90, 65, 15, 1, 0],
                [0, 1, 63, 301, 350, 140, 21, 1, 0],
                [0, 1, 127, 966, 1701, 1050, 266, 28, 1, 0],
                [0, 1, 255, 3025, 7770, 6951, 2646, 462, 36, 1, 0],
                [0, 1, 511, 9330, 34105, 42525, 22827, 5880, 750, 45, 1, 0],
            ][n][k]
        ) for n in range(11) for k in range(n+2)
    ]
)
def test_s2(n, k, s):
    assert s2(n, k) == s