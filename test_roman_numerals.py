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
# TEST HERE -->>
def evaluate_length_2(roman_numeral: str, roman_table):
        last_char: int = roman_table[roman_numeral[-1]] 
        first_char: int = roman_table[roman_numeral[0]] 

        if first_char < last_char:
            return last_char - first_char
        else:
            return last_char + first_char

def convert_multiple_letters(roman_numeral:str, roman_table: dict):

    running_decimal_val = 0

    if roman_numeral.startswith("V"): 
        running_decimal_val = roman_table["V"]
        roman_numeral = roman_numeral[1:]

    if ('V' not in roman_numeral) and ('X' not in roman_numeral):
        return len(roman_numeral) + running_decimal_val
    elif len(roman_numeral) == 2:
        return evaluate_length_2(roman_numeral, roman_table)

def convert_roman_numeral(roman_numeral: str) -> int:
    roman_table: dict = {
        'I': 1,
        'V': 5, 
        'X': 10
    }

    if len(roman_numeral) == 1:
        return roman_table[roman_numeral]
    else:
        return convert_multiple_letters(roman_numeral, roman_table)
      
    # II
    # last_char = I = 1
    # I (1) < 1
    # III
    # last_char = 1
    # I -> 1; I -> 1


testdata = [
    ('I',1),
    ('II',2),
    ('III',3),
    ('IV',4),
    ('V',5),
    ('VI',6),
    ('VII',7),
    ("VIII", 8), 
    ("IX", 9),
    ("X", 10),
]
@pytest.mark.parametrize("roman_numeral, expected_int", testdata)
def test_roman_numeral_conversion(roman_numeral, expected_int):
    result = convert_roman_numeral(roman_numeral)
    assert result == expected_int, f"Expected {expected_int}, but got {result}"