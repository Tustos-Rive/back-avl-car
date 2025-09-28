import random as rd

class RandomsUtils:
    @staticmethod
    def random_id(length: int, int_every: int | None = None, capital: bool = True) -> str:
        key, rd_letter, rd_int = '', '', -1

        for i in range(length):
            # Add a random capital letter
            rd_letter = RandomsUtils.random_letter(capital)

            if int_every:
                # It's in the position "int_every" => int_every = 2; par positions, every 2 positions
                if i % int_every == 0:
                    # Generate and add random int
                    rd_int = RandomsUtils.random_int(0, 9)
                    key += str(rd_int)
                else:
                    key += rd_letter
            else:
                key += rd_letter
        return key

    @staticmethod
    def random_letter(capital: bool = True) -> str:
        letter, __randint = '', -1
        
        range_ascii_capital = [65, 90]
        range_ascii = [97, 122]

        # CAPITAL letters by default
        __default = range_ascii_capital

        if not capital:
            # Change to !CAPITAl letter
            __default = range_ascii

        # Generate a random int inside range...
        __randint = rd.randint(__default[0], __default[1])
        letter = chr(__randint)

        return letter
    
    @staticmethod
    def random_int(start: int, end: int) -> int:
        return rd.randint(start, end)