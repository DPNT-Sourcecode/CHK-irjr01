from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout:
    def test_basic(self):
        total = checkout(["A", "B"])
        assert total == 80
