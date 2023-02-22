from player import Player
import random

class AI(Player):
    def __init__(self):
        self.name = "SkyNet"
        super().__init__()
    
    def shoot(self):
        ai_selection = random.choice(self.shoot_list)
        print(ai_selection)
        return ai_selection