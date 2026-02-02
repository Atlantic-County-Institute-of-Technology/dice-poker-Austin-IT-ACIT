import random
random_value = random.randint(1, 6)


class Dice:
    def __init__(self):
        self.max_dice = 5
        self.dice = []
        self.keep = []

        for die in range(self.max_dice):
            self.dice.append(Die())
            self.keep.append(0)
        
    def get_dice(self):
        return self.dice
    
    def get_keeped(self):
        return self.keep



class Die:

    def __init__(self):
        self.faces = 6
        self.value = 1
        self

    def get_value(self):
        return self.value
    
    
    def roll(self):
        self.value = random.randint(1, self.faces)
        return self.value

    def __str__(self):
        out_string = "Dice about:\n"
        out_string = out_string + f"faces: {self.faces} \n"
        out_string = out_string + f"value: {self.value} \n"
        return out_string