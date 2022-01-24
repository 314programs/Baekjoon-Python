#The tests are coming and I have no time to code
price, amount, money = map(int, input().split())
print(max(0, (price*amount) - money))
