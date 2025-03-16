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

        assert checkout("AAAAA") == 130 + 100
        assert checkout("AAAAAA") == 260

        assert checkout("B") == 30
        assert checkout("BB") == 45

        assert checkout("BBB") == 75
        assert checkout("BBBB") == 90

        assert checkout("ABCDABCD") == 100 + 45 + 40 + 30
        assert checkout("AABBDDCC") == 100 + 45 + 40 + 30

        assert checkout("AAABB") == 130 + 45


# id = CHK_R1_001, req = checkout("ABCDCBAABCABBAAA"), resp = 575


