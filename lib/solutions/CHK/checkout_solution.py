from collections import defaultdict
# noinspection PyUnusedLocal
# skus = unicode string

# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


# assumptions
# sku will come in a consistent case (upper or lower)
def checkout(skus):
    cart = defaultdict(int)
    specials = {
        "3A": 130,
        "2B": 45,
    }

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }
    for sku in skus:
        cart[sku] += 1

    result = 0
    for sku, count in cart.items():
        key = str(count) + sku
        if key in specials:
            result += specials[key]
        else:
            result += prices[sku]
    return result





