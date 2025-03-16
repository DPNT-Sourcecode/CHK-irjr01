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
        # key -> (count, special price)
        "A": (3, 130),
        "B": (2, 45),
    }

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }
    for sku in skus:
        if sku not in prices:
            return -1
        cart[sku] += 1

    result = 0
    for sku, count in cart.items():
        if sku in specials:
            (special_count, special_price) = specials[sku]

            times = count // special_count
            special_rate = times * special_price

            remaining = count % special_count
            remaining_rate = remaining * prices[sku]

            result += special_rate + remaining_rate

        else:
            result += count * prices[sku]
    return result


