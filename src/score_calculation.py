# l = [100, 21, 73, 85, 99, 12, 55, 65, 43]


# def num1():
#     s = max(l)
#     return s


# def num2():
#     s = min(l)
#     return s


# def num3():
#     s = sum(l) / len(l)
#     return s


def max_func():
    best = max([100, 21, 73, 85, 99, 12, 55, 65, 43])
    return best


def min_func():
    worst = min([100, 21, 73, 85, 99, 12, 55, 65, 43])
    return worst


def ave():
    average = sum([100, 21, 73, 85, 99, 12, 55, 65, 43]) / \
        len([100, 21, 73, 85, 99, 12, 55, 65, 43])
    return average
