import pytest

"""
Red, Green, Refactor:
- Write a test that faiils
- Make it pass
- Refactor
---------------
I - 1
II - 2
III - 3
IV - 4
V - 5
VI - 6
VII - 7
VIII - 8
IX - 9
X - 10


XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX

"""

def convert_roman_numeral(roman_numeral: str) -> int:
    return len(roman_numeral)


testdata = [
    ('I',1),
    ('II',2)
]
@pytest.mark.parametrize("roman_numeral, expected_int", testdata)
def test_roman_numeral_conversion(roman_numeral, expected_int):
    result = convert_roman_numeral(roman_numeral)
    assert result == expected_int, f"Expected {expected_int}, but got {result}"