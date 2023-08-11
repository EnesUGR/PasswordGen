import password_strength.tests
from password_strength import PasswordPolicy


class Checking:
    def __init__(self, password_text:str, length=8,uppercase=2,numbers=2,special=2,nonletters=2,entropybits=30,strength=0.66):
        policy = PasswordPolicy.from_names(
            length=length,
            uppercase=uppercase,
            numbers=numbers,
            special=special,
            nonletters=nonletters,
            entropybits=entropybits, #Value that defines how much variety it has
            strength=strength #Complexity; range of 0.00..0.99. Good starting at 0.66
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
        definitaions = {'L': 'Letter', 'M': 'Mark', 'N': 'Number', 'P': 'Punctuation', 'S': 'Symbol', 'Z': 'Separator', 'C': 'Other'}
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
            "score":str(score),
            "eabits":str(eabits),
            "weak":str(weak),
            "length":str(length),
            "letters":str(letters),
            "uppercase":str(uc),
            "lowercase":str(lc),
            "specialcase":str(sc),
            "nums":str(nums),
            "repeatedpattern":str(rp),
            "chars":chars,
            "combs":str(combs)
        }
        return result

