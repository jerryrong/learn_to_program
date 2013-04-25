def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    buses = 0
    if n % 50 != 0:
        buses = n // 50 + 1
    else:
        buses = n // 50 
    return buses



def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    first_item = 0
    second_item = 0

    for item in price_changes:
        if item > 0:
            first_item += item
        elif item < 0:
            second_item += item

    return (first_item, second_item)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    L[:k], L[-k:] = L[-k:], L[:k]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
