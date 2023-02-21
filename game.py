class Game:
    def __init__(self):
        self.gestures=['rock','paper','scissors','lizard','spock']
        pass
    def run_game(self):
        self.display_welcome()
        pass
    def display_welcome(self):
        print('Welcome to RPSLS!')
    def display_rules(self):
        print(f'Here are the rules!\ngiven the five gestures: \n{self.gestures}\nthe given player selects one per round: this game is best out of three.\n ')
    def rounds(self):
        user_input=input('Single or Multi Player?(1 for single, 2 for multi)')
        if user_input==1:
            pass
        elif user_input==2:
            player1=input('what is player one name? ')
            player2=input('what is player two name? ')
            p1=0
            p2=0
            while p1!=2 or p2!=2:
                
            pass
    