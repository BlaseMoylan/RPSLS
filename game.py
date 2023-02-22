from human import Human
from ai import AI
class Game:
    def __init__(self):
        self.display_welcome()
        
    def run_game(self):
        self.display_rules()
        self.rounds()
        
    def display_welcome(self):
        print('Welcome to RPSLS!')

    def display_rules(self):
        print(f'Here are the rules!\ngiven the five gestures: \n(Rock,Paper,Scissors,Lizard,Spock)\nthe given player selects one per round: this game is best out of three.\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n')
    
    def rounds(self):
        user_input=input('Single or Multi Player?(1 for single, 2 for multi)')
        if user_input=='1':
            self.player1=Human(input('what is the player name? '))
            self.player2=AI()
            player1_name=self.player1.human_player
            ai_name=self.player2.name
            self.round(player1_name,ai_name)
            
        elif user_input=='2':
            self.player1=Human(input('what is player one name? '))
            self.player2=Human(input('what is player two name? '))
            player1_name=self.player1.human_player
            player2_name=self.player2.human_player
            self.round(player1_name,player2_name)

    def which_gestor_wins(self,player1,player2):
        if player1=='Rock'and (player2=='Paper' or player2 =='Spock'):
            return player2
        elif player1=='Paper' and (player2=='Lizard' or player2=='Scissors'):
            return player2
        elif player1=='Scissors' and (player2=='Spock' or player2=='Rock'):
            return player2
        elif player1=='Lizard' and (player2=='Rock' or player2=='Scissors'):
            return player2
        elif player1=='Spock' and (player2=='Lizard' or player2=='Paper'):
            return player2
        else:
            return player1

    def round(self,player1_name,player2_name):
        p1=0
        p2=0
        while p1!=2 and p2!=2:
            player1_shoot=self.player1.shoot()
            player2_shoot=self.player2.shoot()
            win=self.which_gestor_wins(player1_shoot,player2_shoot)
            if player1_shoot!=player2_shoot:
                if player1_shoot==win:
                    p1+=1
                    print(f'round winner: {player1_name}')
                else:
                    p2+=1
                    print(f'round winner: {player2_name}')
            else:
                print('Tie!')

        if p1==2:
            print(f'the winner is: {player1_name}')
        else:
            print(f'the winner is: {player2_name}')
