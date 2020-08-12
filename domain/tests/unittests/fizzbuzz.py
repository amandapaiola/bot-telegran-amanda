from unittest import TestCase

from domain.fizzbuzz import fizz_buzz


class FizzBuss(TestCase):

    def test_retornaFizzBuzz_com_1(self):
        assert fizz_buzz(1) == 1

    def test_retornaFizzBuzz_com_2(self):
        assert fizz_buzz(2) == 2

    def test_retornaFizzBuzz_com_3(self):
        assert fizz_buzz(3) == 'fizz'

    def test_retornaFizzBuzz_com_4(self):
        assert fizz_buzz(4) == 4

    def test_retornaFizzBuzz_com_5(self):
        assert fizz_buzz(5) == 'buzz'

    def test_retornaFizzBuzz_com_6(self):
        assert fizz_buzz(6) == 'fizz'

    def test_retornaFizzBuzz_com_7(self):
        assert fizz_buzz(7) == 7

    def test_retornaFizzBuzz_com_8(self):
        assert fizz_buzz(8) == 8

    def test_retornaFizzBuzz_com_9(self):
        assert fizz_buzz(9) == 'fizz'

    def test_retornaFizzBuzz_com_10(self):
        assert fizz_buzz(10) == 'buzz'

    def test_retornaFizzBuzz_com_11(self):
        assert fizz_buzz(11) == 11

    def test_retornaFizzBuzz_com_12(self):
        assert fizz_buzz(12) == 'fizz'

    def test_retornaFizzBuzz_com_13(self):
        assert fizz_buzz(13) == 13

    def test_retornaFizzBuzz_com_14(self):
        assert fizz_buzz(14) == 14

    def test_retornaFizzBuzz_com_15(self):
        assert fizz_buzz(15) == 'fizz-buzz'

    def test_retornaFizzBuzz_com_25(self):
        assert fizz_buzz(25) == 'buzz'

    def test_retornaFizzBuzz_com_30(self):
        assert fizz_buzz(30) == 'fizz-buzz'

    def test_retornaFizzBuzz_com_99(self):
        assert fizz_buzz(99) == 'fizz'

    def test_retornaFizzBuzz_com_125(self):
        assert fizz_buzz(125) == 'buzz'
