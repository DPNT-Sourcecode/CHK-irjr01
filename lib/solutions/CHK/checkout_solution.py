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
def checkout_one(skus):
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


# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+
def checkout(skus):
    cart = defaultdict(int)
    specials = {
        # key -> [(count, special price)]
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
    }

    bogo_specials = {
        # key -> [(count, special price)]
        "E": ("B", 1)
    }

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }
    for sku in skus:
        if sku not in prices:
            return -1
        cart[sku] += 1

    # applying these specials favors the customers more
    for sku in skus:
        if sku in bogo_specials:
            (discount_sku, discount_count) = bogo_specials[sku]
            cart[discount_sku] -= discount_count

    result = 0
    for sku, count in cart.items():
        current_count = count
        while current_count > 0:
            print(f"{current_count=}")
            if sku in specials:
                for deal in specials[sku]:
                    (special_count, special_price) = deal
                    print(f"{special_count=} {special_price=}")

                    times = current_count // special_count
                    special_rate = times * special_price
                    print(f"{times=} {special_rate=}")

                    # remaining = current_count % special_count
                    # remaining_rate = remaining * prices[sku]

                    result += special_rate
                    print(f"{result=}")
                    current_count -= special_count
                    print(f"after disvount {current_count=}")

                if current_count > 0:
                    remaining_non_specials = count * prices[sku]
                    result += remaining_non_specials

            else:
                result += count * prices[sku]

    return result

