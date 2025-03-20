from board import Board
from player import Player

class TicTacToeGame:
    
    def start(self):
        
        print('******************')
        print('Welcome to Tic Tac Toe!')
        print('******************')
        
        board = Board()
        player = Player()
        computer = Player(False)
        
        while True:
            board.print_board()
            while True:
                
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()
                
                if board.check_tie() and not board.check_is_game_over(player, player_move) or board.check_tie() and not board.check_is_game_over(computer, player_move):
                    print('It\'s a tie!')
                    break
                elif board.check_is_game_over(player, player_move):
                    print('Congrats! You won th game!')
                    break
                else:
                    
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()
                    
                    if board.check_is_game_over(computer, computer_move):
                        print('Ooops... computer won the game!')
                        break
                    
            play_again = input('Woulf you like to play again? Enter X for YES or O fro No: ').upper()
            
            if play_again == "O":
                print('Bye! Come back soon.')
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print('Invalid input. Startin a new game.')
                self.start_new_round(board)
                
    def start_new_round(self, board):
        print('Starting a new round...')
        board.reset_board()
        board.print_board()
        
game = TicTacToeGame()
game.start()