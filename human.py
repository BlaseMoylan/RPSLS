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
        user_input=False
        while user_input == False:
            shoot_input=input("Which option do you want to choose? ")
            if shoot_input.isnumeric():
                choose_shoot = int(shoot_input)
                if choose_shoot <5:
                    if choose_shoot==0:
                        print(f"{self.human_player} chooses Rock.")
                    elif choose_shoot==1:
                        print(f"{self.human_player} chooses Paper.")
                    elif choose_shoot==2:
                        print(f"{self.human_player} chooses Scissors.")
                    elif choose_shoot==3:
                        print(f"{self.human_player} chooses Lizard.")
                    elif choose_shoot==4:
                        print(f"{self.human_player} chooses Spock.")
                    user_input=True
                else:
                    print('invalid range please choose between 0 and 4! ')
            else:
                print('You did not enter a valid input! ')
