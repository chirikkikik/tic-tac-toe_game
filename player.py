from move import Move
import random

class Player:
    
    PLAYER_MARKER = 'X'
    COMPUTER_MARKER = 'O'
    
    def __init__(self, is_human=True):
        self._is_human = is_human
        
        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER
        
    @property
    def is_human(self):
        return self._is_human
        
    @property
    def marker(self):
        return self._marker
    
    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
        
    def get_human_move(self):
        while True:
            user_input = int(input('Enter a number between 1 and 9: '))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print('Please enter number between 1 and 9.')
                
        return move
                
    def get_computer_move(self):
        computer_input = random.choice(list(range(1, 10)))
        move = Move(computer_input)
        print('Computer move:', computer_input)
        return move
            
 
    