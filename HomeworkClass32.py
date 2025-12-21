class IntegerToRoman:
    def __init__(self):
        self.roman_map = {
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
    def convert(self, num: int) -> str:
        """
        Converts an integer to a Roman numeral.
        """
        result = ""
        for value, symbol in self.roman_map.items():
            while num >= value:
                result += symbol
                num -= value
        return result