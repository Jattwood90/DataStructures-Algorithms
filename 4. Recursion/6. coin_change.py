# This solution is totally inefficient - tried 63 which took a long time.

def coin(target,coins):

    # default value set to target
    min_coins = target

    # checks to see if target is in coin values list
    if target in coins:
        return 1
    else:
    # for every coin values that are less than or equal to my target
        for i in [c for c in coins if c <= target]:

            # add coin count + recursive call
            num_coins = 1 + coin(target-i, coins)

            # reset minimum if new_num coins in less than min_coins
            if num_coins < min_coins:

                min_coins = num_coins

    return min_coins


def rec_coin_dynam(target, coins, known_results):

    # default output to target
    min_coins = target

    # base case
    if target in coins:
        known_results[target] = 1
        return 1
    # retunn a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:

        for i in [c for c in coins if c<= target]:

            num_coins = 1 + rec_coin_dynam(target-i, coins, known_results)
            if num_coins < min_coins:
                min_coins = num_coins

                # reset known result
                known_results[target] = min_coins
    return min_coins
target = 84
known_results = [0]*(target+1)
print(rec_coin_dynam(target, [1,2,5,10,25],known_results))
