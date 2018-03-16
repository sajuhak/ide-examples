class RomanNumeralConverter(object):
    """
    The Roman Numeral Converter only applies rules of addition.
    """

    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.digit_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    # TODO: Implement Substraction

    def convert_to_decimal(self):
        val = 0
        for char in self.roman_numeral:
            val += self.digit_map[char]
        return val


def test_parsing_millenia():
    value = RomanNumeralConverter("M")
    assert value.convert_to_decimal() == 1000


def test_parsing_half_millenia():
    value = RomanNumeralConverter("D")
    assert value.convert_to_decimal() == 500


def test_parsing_century():
    value = RomanNumeralConverter("C")
    assert value.convert_to_decimal() == 100


def test_parsing_half_century():
    value = RomanNumeralConverter("L")
    assert value.convert_to_decimal() == 50


def test_parsing_decade():
    value = RomanNumeralConverter("X")
    assert value.convert_to_decimal() == 10


def test_parsing_half_decade():
    value = RomanNumeralConverter("V")
    assert value.convert_to_decimal() == 5

# FIXME: Test Fails
def test_parsing_one():
    value = RomanNumeralConverter("I")
    assert value.convert_to_decimal() == 2
