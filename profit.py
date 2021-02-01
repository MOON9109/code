prices=[7,1,5,3,6,4]

def maxprice(x):
    profit =0
    minprice=9999999



    for price in x:
        minprice = min(price, minprice)
        
        profit=max(profit,price-minprice)
        
    return profit
print(maxprice(prices))
