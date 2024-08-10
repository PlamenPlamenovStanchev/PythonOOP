from itertools import permutations


def possible_permutations(ls):
    for permutation in permutations(ls):
        yield list(permutation)

    # if len(ls) <= 1:
    #     yield ls
    # else:
    #     for i in range(len(ls)):
    #         for permutation in possible_permutations(ls[:i] + ls[i + 1]):
    #             yield [ls[i]] + permutation



