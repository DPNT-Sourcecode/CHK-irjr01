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

    def test_five_as(self):
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

    def test_one(self):
        assert checkout("") == 0
        assert checkout("A") == 50
        assert checkout("B") == 30
        assert checkout("C") == 20
        assert checkout("D") == 15
        assert checkout("a") == -1
        assert checkout("-") == -1

        assert checkout("ABCa") == -1
        assert checkout("AxA") == -1

        assert checkout("ABCD") == 115
        assert checkout("A") == 50
        assert checkout("AA") == 100

        assert checkout("AAA") == 130
        assert checkout("AAAA") == 180

        assert checkout("AAAAA") == 250
        assert checkout("AAAAAA") == 300

        assert checkout("B") == 30
        assert checkout("BB") == 45

        assert checkout("BBB") == 90
        assert checkout("BBBB") == 120


# defaultdict(<class 'int'>, {'B': 3})
# id = CHK_R1_020, req = checkout("BBB"), resp = 90
# defaultdict(<class 'int'>, {'B': 4})
# id = CHK_R1_021, req = checkout("BBBB"), resp = 120
# defaultdict(<class 'int'>, {'A': 2, 'B': 2, 'C': 2, 'D': 2})
# id = CHK_R1_022, req = checkout("ABCDABCD"), resp = 215
# defaultdict(<class 'int'>, {'B': 2, 'A': 2, 'D': 2, 'C': 2})
# id = CHK_R1_023, req = checkout("BABDDCAC"), resp = 215
# defaultdict(<class 'int'>, {'A': 3, 'B': 2})
# id = CHK_R1_024, req = checkout("AAABB"), resp = 175
# defaultdict(<class 'int'>, {'A': 7, 'B': 5, 'C': 3, 'D': 1})
# id = CHK_R1_001, req = checkout("ABCDCBAABCABBAAA"), resp = 575
