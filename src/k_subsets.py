
def k_subsets(s: set, k: int):
    return list(_k_subsets(s, k))


def _k_subsets(s: set, k: int):
    """
    Yields:
        Solutions, each of which is a list of sets
    """
    n = len(s)
    if n == 0 and k == 0:
        yield []  # One solution containing k == 0 partitions
        return
    if k == 0:
        return
    if n == 0:
        return
    if k == 1:
        yield [s]
        return
    if n == k:
        yield [{e} for e in s]
        return
    for e in s:
        singleton = {e}
        remainder = s - singleton
        for recurrence in _k_subsets(remainder, k):
            for i in range(len(recurrence)):
                pre, ith, post = recurrence[:i], recurrence[i], recurrence[i+1:]
                result = [*pre, ith | singleton, *post]
                print(f"{singleton = }, {remainder = }, {recurrence = }, {i = }, {result = }")
                yield result


def dedup(seq_of_sets):
    f_sets = frozenset(frozenset(s) for s in seq_of_sets)
    assert len(f_sets) == len(seq_of_sets)
    return f_sets



#  {1, 2} -> [{1} {2}] P

#  {1, 2, 3} -> [{1} {2, 3}]  PR   A
#               [{1, 3} {2}]  PL   B
#               [{3} {1, 2}]  --   C

#  {1, 2. 3. 4} -> [{1}, {2, 3, 4}] AR
#                  [{2}, {1, 3, 4}] BR
#                  [{3}, {1, 2, 4}] CR
#                  [{4}, {1, 2, 3}] --
#                  [{1, 4}, {2, 3}] AL
#                  [{2, 4}, {1, 3}] BL
#                  [{3, 4}, {1, 2}] CL

# Recurence has same k but a smaller set
# For each result in the recurrence, insert the singleton into
# each group in turn, including the empty set.