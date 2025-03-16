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
        assert total == 130 + 45 + 14
