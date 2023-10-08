def maxrevenue(length, price, l, opt_rev=dict()):
    opt_rev[length[0]] = price[0]
    
    for i in range(1,len(length)):
        if length[i] in opt_rev.keys():
            a = opt_rev[length[i]]
        else:
            a = max(a+price[0],opt_rev[i])
            opt_rev[length[i]] = a
        if length[i] == l:
            return a
    return a
    return opt_prices[8] + maxrevenue(length,price,l-8,opt_prices)'''

length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]
l = 10

#print(maxrevenue(length, price, l))
opt_prices = {8:20}
if 8 in opt_prices.keys():
    print(opt_prices[8])