class Game:
    def __init__(self):
        self.gestures=['rock','paper','scissors','lizard','spock']
        
    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.rounds()
        
    def display_welcome(self):
        print('Welcome to RPSLS!')
    def display_rules(self):
        print(f'Here are the rules!\ngiven the five gestures: \n{self.gestures}\nthe given player selects one per round: this game is best out of three.\n ')
    def rounds(self):
        user_input=input('Single or Multi Player?(1 for single, 2 for multi)')
        # if user_input==1:
        #     pass
        if user_input=='2':
            player1_name=input('what is player one name? ')
            player2_name=input('what is player two name? ')
            p1=0
            p2=0
            while p1!=2 and p2!=2:
                player1_shoot=input(f'select one of the following: {self.gestures}')
                player2_shoot=input(f'select one of the following: {self.gestures}')
                if player1_shoot==self.which_gestor_wins(player1_shoot,player2_shoot):
                    p1+=1
                else:
                    p2+=1
            if p1==2:
                print(f'the winner is: {player1_name}')
            else:
                print(f'the winner is: {player2_name}')

    def which_gestor_wins(self,player1,player2):
        if player1=='rock'and player2=='paper' or player2 =='spock':
            return player2
        elif player1=='scissors' and player2=='spock' or player2=='rock':
            return player2
        elif player1=='paper' and player2=='lizard' or player2=='scissors':
            return player2
        elif player1=='lizard' and player2=='rock' or player2=='scissors':
            return player2
        elif player1=='spock' and player2=='lizard' or player2=='paper':
            return player2
        else:
            return player1

