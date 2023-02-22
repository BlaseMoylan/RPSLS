from human import Human
from ai import AI
class Game:
    def __init__(self):
        self.display_welcome()
        self.player1=Human(input('what is player one name? '))
        self.player2=Human(input('what is player two name? '))
        self.ai=AI()
        
    def run_game(self):
        self.display_rules()
        self.rounds()
        
    def display_welcome(self):
        print('Welcome to RPSLS!')

    def display_rules(self):
        print(f'Here are the rules!\ngiven the five gestures: \n{self.player1.shoot_list}\nthe given player selects one per round: this game is best out of three.\n ')
    
    def rounds(self):
        user_input=input('Single or Multi Player?(1 for single, 2 for multi)')
        if user_input=='1':
            player1_name=self.player1.human_player
            ai_name=self.ai.name
            p1=0
            p2=0
            while p1!=2 and p2!=2:
                player1_shoot=self.player1.shoot()
                ai=self.ai.choose_gesture()
                win=self.which_gestor_wins(player1_shoot,ai)
                if player1_shoot==win:
                    p1+=1
                else:
                    p2+=1
            if p1==2:
                print(f'the winner is: {player1_name}')
            else:
                print(f'the winner is: {ai_name}')
        if user_input=='2':
            player1_name=self.player1.human_player
            player2_name=self.player2.human_player
            p1=0
            p2=0
            while p1!=2 and p2!=2:
                player1_shoot=self.player1.shoot()
                player2_shoot=self.player2.shoot()
                win=self.which_gestor_wins(player1_shoot,player2_shoot)
                if player1_shoot==win:
                    p1+=1
                else:
                    p2+=1
            if p1==2:
                print(f'the winner is: {player1_name}')
            else:
                print(f'the winner is: {player2_name}')

    def which_gestor_wins(self,player1,player2):
        if player1=='Rock'and player2=='Paper' or player2 =='Spock':
            return player2
        elif player1=='Scissors' and player2=='Spock' or player2=='Rock':
            return player2
        elif player1=='Paper' and player2=='Lizard' or player2=='Scissors':
            return player2
        elif player1=='Lizard' and player2=='Rock' or player2=='Scissors':
            return player2
        elif player1=='Spock' and player2=='Lizard' or player2=='Paper':
            return player2
        else:
            return player1

