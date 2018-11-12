

result = 0

def change(target, coins, index=0, count=0, maxcount=15):
    global result
    if target< 0 or count > maxcount:
        return
    if target == 0:
        result += 1
        # print(count)
        return
    if index >= len(coins):
        return
    for i in range(int(target/coins[index])+1):
        change(target-i*coins[index], coins, index+1, count+i, maxcount)

def main():

    print(result)
    target = 1000
    coins = [10,50,100,500]
    coins = sorted(coins,reverse=True)
    change(target,coins)
    print(result)

if __name__ == '__main__':
    main()
