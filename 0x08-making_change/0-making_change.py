#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ makeChange """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coins_used = 0
    amount_checked = 0

    for coin in coins:
        while amount_checked < total:
            amount_checked += coin
            coins_used += 1

        if amount_checked == total:
            return coins_used

        amount_checked -= coin
        coins_used -= 1

    return -1
