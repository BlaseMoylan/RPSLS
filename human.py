from player import Player
import random

class Human(Player):
    def __init__(self, name):
        self.human_player = name
        super().__init__()
        
    def shoot(self):
        # If we can let's make this 1-5
        print("")
        print("Select 0 for Rock")
        print("Select 1 for Paper")
        print("Select 2 for Scissors")
        print("Select 3 for Lizard")
        print("Select 4 Spock")
        print("")
        user_input=False
        counter = 0
        while user_input == False and counter < 6:
            shoot_input=input("Which option do you want to choose? ")
            if shoot_input.isnumeric():
                choose_shoot = int(shoot_input)
                if choose_shoot <5 and counter < 5:
                    if choose_shoot==0:
                        print(f"{self.human_player} chooses Rock.")
                        return("Rock")
                    elif choose_shoot==1:
                        print(f"{self.human_player} chooses Paper.")
                        return ("Paper")
                    elif choose_shoot==2:
                        print(f"{self.human_player} chooses Scissors.")
                        return ("Scissors")
                    elif choose_shoot==3:
                        print(f"{self.human_player} chooses Lizard.")
                        return ("Lizard")
                    elif choose_shoot==4:
                        print(f"{self.human_player} chooses Spock.")
                        return ("Spock")
                    user_input=True
                elif counter > 4:
                    print(f"{self.human_player} has been assigned {random.choice(self.shoot_list)}!")
                    return (random.choice(self.shoot_list))
                else:
                    print('invalid range please choose between 0 and 4! ')
                    counter += 1
            else:
                print('You did not enter a valid input! ')
                counter += 1
