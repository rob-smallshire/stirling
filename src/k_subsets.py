import logging

logger = logging.getLogger(__name__)

# Given a set {1, 2, 3, 4} and the requirement to partition it into k=3 non-empty
# subsets, solutions can be generated from small sub problems in two ways:
#
# First, we can ask for one fewer (k=2) partitions of a smallser set {1, 2, 3} that
# excludes a singleton element {4},
#
#  [{1, 2}, {3}]
#  [{1, 3}, {2}]
#  [{1}, {2, 3}]
#
# we can generate solutions to the original problem by adding back the singleton to
# each result give four partitions:
#
#  [{1, 2}, {3}, {4}]
#  [{1, 3}, {2}, {4}]
#  [{1}, {2, 3}, {4}]
#
# The second way of reducing problem is to ask for k=3 partitions of the smaller
# set which excludes the singleton. In this case there is only one such solution:
#
#  [{1}, {2}, {3}]
#
# We can then add the element of the singleton set back to each partition of this
# result in turn, generating a further three solutions to the original problem:
#
#  [{1, 4}, {2}, {3}]
#  [{1}, {2, 4}, {3}]
#  [{1}, {2}, {3, 4}]
#
# This gives a total of six solutions.
#
# The number of solutions to S(4, 3) is therefore the number of solutions to S(3, 2) plus
# the number of solutions to S(3, 3) multiplied by k, which in general is,
#
#  S(n+1, k)  =  S(n, k-1)  +  k * S(n, k)
#
# This is the recurrence relation given in the Wikipedia article
# <https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind>, albeit with the two
# terms transposed.
#
# In the code below it's more convenient to express this recurrence relation with n reduced
# by one as,
#
#  S(n, k)  =  S(n-1, k-1)  +  k * S(n-1, k)

def k_subsets(s: list, k: int):
    return list(_k_subsets(s, k))


def _k_subsets(s: list, k: int):
    """
    Yields:
        Solutions, each of which is a list of sets
    """
    logger.debug("_k_subsets(%r, %r)", s, k)
    n = len(s)
    if n == 0 and k == 0:
        yield [s]  # One solution containing k == 0 partitions
        return
    if k == 0:
        return
    if n == 0:
        return
    if k == 1:
        yield [s]
        return
    if k == n:
        yield [[e] for e in s]
        return

    # Consider the recurrence relation S(n, k) = S(n-1, k-1) + k.S(n-1, k)
    # This is so because the solutions for S(n, k) comprise two kinds of
    # results based on subproblems which are smaller by omitted a single
    # element. We set aside this singleton element from s, to produce the
    # smaller remiander set.

    *remainder, singleton = s

    # The first kind of solution is that enumerated by the first term of the
    # recurrence relation giving S(n-1, k-1) solutions to the sub-problem.
    # For each of these solutions, we can add the singleton back in to produce
    # a solution to the larger problem.
    for p in _k_subsets(remainder, k - 1):
        yield p + [[singleton]]

    # The second kind of solution is that enumerated by the second term of
    # the recurrence relation giving S(n-1, k) solutions to the sub-problem.
    # For each of these solutions to the sub-problem we generate k solutions
    # by incorporating the singleton element into each partition of the
    # solution in turn.
    for q in _k_subsets(remainder, k):
        for i in range(k):
            yield [*q[:i], q[i] + [singleton], *q[i+1:]]
