import random
import timeit

TAX_RATE = .08

txns = [random.randrange(100) for _ in range(1000000)]

def get_price(txn):
    return txn * (1 + TAX_RATE)

def get_price_comprehension():
    return [get_price(txn) for txn in txns]

def get_price_map():
    return list(map(get_price,txns))

def get_price_loop():
    price = []
    for txn in txns:
        price.append(txn)
    return price






