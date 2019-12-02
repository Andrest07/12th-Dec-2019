prices = {0: {'name':'banana', 'price':4, 'stock':5}, 1: {'name':'apple', 'price':2, 'stock':0}, 2: {'name':'orange', 'price':1.5, 'stock':3},3 : {'name':'pear', 'price':3, 'stock':4}}

for i in prices:
    print(prices[i]['name'])
    print("price: " + str(prices[i]['price']))
    print("stock: " + str(prices[i]['stock']))
    print("")

total = 0
for i in prices:
    total = total + (prices[i]['price'] * prices[i]['stock'])
print("Total :" + str(total))