from lib.solutions.CHK.checkout_solution import checkout_one
from lib.solutions.CHK.checkout_solution import checkout


class TestCheckoutOne:
    def test_basic(self):
        total = checkout_one(["A", "B"])
        assert total == 80

    def test_specials(self):
        total = checkout_one(["A", "B", "A", "A"])
        assert total == 160

    def test_two_specials(self):
        total = checkout_one(["A", "B", "A", "A", "B", "D"])
        assert total == 130 + 45 + 15

    def test_invalid_input(self):
        total = checkout_one(["A", "B", "A", "A", "B", "D", "9"])
        assert total == -1

    def test_multiple_items(self):
        total = checkout_one("AA")
        assert total == 100

    def test_partial_special(self):
        total = checkout_one("AAAA")
        assert total == 180

    def test_five_as(self):
        total = checkout_one("AAAAA")
        assert total == 230

    def test_multiple_specials(self):
        total = checkout_one("AAAAAA")
        assert total == 260

    def test_multiple_specials_two(self):
        total = checkout_one("AAAAAAADBBB")
        # 2 A specials
        # 1 remaining A
        # 1 B special
        # 1 remaining B
        # 1 D
        assert total == 260 + 50 + 15 + 45 + 30

    def test_one(self):
        assert checkout_one("") == 0
        assert checkout_one("A") == 50
        assert checkout_one("B") == 30
        assert checkout_one("C") == 20
        assert checkout_one("D") == 15
        assert checkout_one("a") == -1
        assert checkout_one("-") == -1

        assert checkout_one("ABCa") == -1
        assert checkout_one("AxA") == -1

        assert checkout_one("ABCD") == 115
        assert checkout_one("A") == 50
        assert checkout_one("AA") == 100

        assert checkout_one("AAA") == 130
        assert checkout_one("AAAA") == 180

        assert checkout_one("AAAAA") == 130 + 100
        assert checkout_one("AAAAAA") == 260

        assert checkout_one("B") == 30
        assert checkout_one("BB") == 45

        assert checkout_one("BBB") == 75
        assert checkout_one("BBBB") == 90

        assert checkout_one("ABCDABCD") == 100 + 45 + 40 + 30
        assert checkout_one("AABBDDCC") == 100 + 45 + 40 + 30

        assert checkout_one("AAABB") == 130 + 45

    def test_double_discount(self):
        assert checkout_one("AAABB") == 130 + 45


# id = CHK_R1_001, req = checkout("ABCDCBAABCABBAAA"), resp = 575
#




