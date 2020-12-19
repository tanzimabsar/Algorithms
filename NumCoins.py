def numCoins(cents):
    
    coins = [25, 10, 5, 1]

    result = 0

    for index, x in enumerate(coins):

        if cents % x == 0 and index == 0:
            return 1

        elif cents % x == 0:
            result += 1

        elif cents % x == cents:
            pass

        elif cents % x > 0:
            cents = cents % x
            result += 1 

        

    return result


print(numCoins(31))