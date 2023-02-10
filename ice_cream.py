'''
coupon_list = [(1, 2), (3,5), (7, 9)]

find_price(n, coupon_list)
'''

"""
Suppose you're in an ice cream shop with an unusual pricing structure.
- Coupon A: 1 ice cream for $2
- Coupon B: 3 ice creams for $5
- Coupon C: 7 ice creams for $9

Write a function that computes the minimum cost to purchase N ice creams
For example: N=5 -> 9
(2*A + B) # your function doesn't need to produce this

# Extend the function to work for an arbitrary set of coupons.
find_price(num_ic, coupons)

[(1, 2), (3, 5), (7, 9)]
"""
# coupon_list = [(1, 2), (3, 5), (7, 9)]  #cost per ice cream decrease with ice creams

# coupon_list = [(1,2), (2, 2), (5, 6)]

coupon_list = [(1, 1000), (4, 4), (10, 10)]

def find_price(num_ic, coupon_list):
    cheapest_ic_list = sorted(coupon_list, key = lambda x: x[1]/x[0])

    price = 0
    for coupon in cheapest_ic_list:
        num = int(num_ic / coupon[0])
        price = price + num * coupon[1]

        num_ic = num_ic % coupon[0]  # 13%7 = 6

    if num_ic != 0:
        for coupon in cheapest_ic_list:
            if num_ic > 0 and coupon[0] > num_ic:
                price = price + coupon[1]
                num_ic = 0

    return price, num_ic == 0

def find_price2(num_ic, coupon_list):
    sorted_list = sorted(coupon_list)

    min_price, can_buy_all = find_price(num_ic, sorted_list)

    for i in range(1, len(sorted_list)):
        small_list_price, can_buy_all = find_price(num_ic, sorted_list[i:])

        if can_buy_all and small_list_price < min_price:
            can_buy_all = True
            min_price = small_list_price

    if not can_buy_all: return -1

    return min_price

for i in range(1, 25):
    print(f"{i}: {find_price2(i, coupon_list)}")