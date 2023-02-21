from player import Player
import random

class AI(Player):
    def __init__(self):
        self.name = "SkyNet"
    
    def choose_gesture(self):
        ai_selection = random.choice(self.shoot_list)
        return ai_selection