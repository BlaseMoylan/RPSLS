from player import Player

class Human(Player):
    def __init__(self, name):
        self.human_player = name
        super().__init__()
        
def shoot(self):
    # If we can let's make this 1-5
    print("Select 0 for Rock")
    print("Select 1 for Paper")
    print("Select 2 for Scissors")
    print("Select 3 for Lizard")
    print("Select 4 Spock")
    print("")
    
    choose_shoot = int(input("Which option do you want to choose? "))
    
    for gesture in self.shoot_list:
        if gesture == self.shoot_list[0]:
            print(f"{self.human_player} chooses Rock.")
        if gesture == self.shoot_list[1]:
            print(f"{self.human_player} chooses Paper.")
        if gesture == self.shoot_list[2]:
            print(f"{self.human_player} chooses Scissors.")
        if gesture == self.shoot_list[3]:
            print(f"{self.human_player} chooses Lizard.")
        if gesture == self.shoot_list[4]:
            print(f"{self.human_player} chooses Spock.")