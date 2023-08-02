import password_strength.tests
from password_strength import PasswordPolicy


class Checking:
    def __init__(self, password_text:str):
        policy = PasswordPolicy.from_names(
            length=8,
            uppercase=2,
            numbers=2,
            special=2,
            nonletters=2,
            entropybits=30, #Value that defines how much variety it has
            strength=0.66 #Complexity; range of 0.00..0.99. Good starting at 0.66
        )

        self.password = policy.password(password_text)

    def get_result(self) -> bool:
        r = self.password.test()
        if len(r) == 0:
            return True
        else:
            return False

    def get_detailes(self) -> dict:
        score = round(self.password.strength(),4)
        eabits = self.password.entropy_bits
        weak = self.password.weakness_factor

        chars = dict()
        definitaions = {'L': 'letter', 'M': 'Mark', 'N': 'Number', 'P': 'Punctuation', 'S': 'Symbol', 'Z': 'Separator', 'C': 'Other'}
        for _ in list(self.password.char_categories.items()):
            chars[definitaions[_[0]]] = _[1]

        combs = self.password.combinations
        nums = self.password.numbers
        letters = self.password.letters
        uc = self.password.letters_uppercase
        lc = self.password.letters_lowercase
        sc = self.password.special_characters
        rp = self.password.repeated_patterns_length
        length = self.password.length

        result = {
            "score":score,
            "eabits":eabits,
            "weak":weak,
            "chars":chars,
            "combs":combs,
            "nums":nums,
            "letters":letters,
            "uppercase":uc,
            "lowercase":lc,
            "specialcase":sc,
            "repeatedpattern":rp,
            "length":length
        }
        return result

