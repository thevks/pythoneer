def nonconstructible_change(coins):
    coins.sort()
    currentChange = 0
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1
        currentChange += coin
    
    return currentChange + 1

if __name__ == '__main__':
    coins = [5,7,1,1,2,3,22]
    print(nonconstructible_change(coins))

    coins = [1,2,5]
    print(nonconstructible_change(coins))
