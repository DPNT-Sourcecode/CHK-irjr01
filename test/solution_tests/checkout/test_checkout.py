from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout:
    def test_basic(self):
        total = checkout(["A", "B"])
        assert total == 80

    def test_specials(self):
        total = checkout(["A", "B", "A", "A"])
        assert total == 160

    def test_two_specials(self):
        total = checkout(["A", "B", "A", "A", "B", "D"])
        assert total == 130 + 45 + 15

    def test_invalid_input(self):
        total = checkout(["A", "B", "A", "A", "B", "D", "9"])
        assert total == -1

    def test_multiple_items(self):
        total = checkout("AA")
        assert total == 100

    def test_partial_special(self):
        total = checkout("AAAA")
        assert total == 180

    def test_three(self):
        total = checkout("AAAAA")
        assert total == 230

    def test_multiple_specials(self):
        total = checkout("AAAAAA")
        assert total == 260

    def test_multiple_specials_two(self):
        total = checkout("AAAAAAADBBB")
        # 2 A specials
        # 1 remaining A
        # 1 B special
        # 1 remaining B
        # 1 D
        assert total == 260 + 50 + 15 + 45 + 30


# - {"method":"checkout","params":["AAAA"],"id":"CHK_R1_015"}, expected: 180, got: 200
# - {"method":"checkout","params":["AAAAA"],"id":"CHK_R1_016"}, expected: 230, got: 250
# - {"method":"checkout","params":["AAAAAA"],"id":"CHK_R1_017"}, expected: 260, got: 300





