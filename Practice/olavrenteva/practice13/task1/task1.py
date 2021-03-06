class NonValidInput(Exception):
    pass


CONVERT_DICT = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }


def to_roman(number):
    if not isinstance(number, int) or number < 1 or number > 5000:
        raise NonValidInput('to_roman function accepts only integers between 1 and 5000')

    roman_num = ''
    for dec, rom in CONVERT_DICT.items():
        roman_num += rom * int(number//dec)
        number = number - dec * (number//dec)

    return roman_num
