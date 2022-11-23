import logging

logger = logging.getLogger(__name__)


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
