
class Game():

    def __init__(self, turn='X', tie=False, winner=False):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print('Welcome to Tic Tac Toe!')

    def print_board(self):
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)

    def print_message(self):
        if self.tie == True:
            print('Tie Game!')
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def place_piece(self):
        move = input(f"Enter a valid move (example: A1): ").lower()
        print(move)
        while True:
            if self.board[move] == 'X' or self.board[move] == 'O':
                input("Invalid input. Please enter a valid input").lower()
            else:
                self.board[move] = self.turn
                self.render()
                break

    def check_winner(self):
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']):
            self.winner = self.board['a1'] 
            
        elif self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']):
            self.winner = self.board['a2']
            
        elif self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']):
            self.winner = self.board['a3']
            
        elif self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']):
            self.winner = self.board['a1']
            
        elif self.board['a3'] and (self.board['a3'] == self.board['b2'] == self.board['c1']):
            self.winner = self.board['a3']
            
        elif self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']):
            self.winner = self.board['a1']
            
        elif self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']):
            self.winner = self.board['b1']
            
        elif self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']):
            self.winner = self.board['c1']
            
        
    def check_for_tie(self):
        board_filled = True
        for key, value in self.board.items():
            if value == None:
                board_filled = False
                break
        if self.winner == False and board_filled == True:
            self.tie = True
            
                

    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        elif self.turn == 'O':
            self.turn = 'X'

    def play_game(self):
        print("Shall we play a game?")
        # While there is no winner or tie
        while self.winner == False and self.tie == False:
        # render
            self.render()
        # get player input
            self.place_piece()
        # check for a winner
            self.check_winner()
        # check for a tie
            self.check_for_tie()
        # switch turns
            if self.winner == False and self.tie == False:
                self.switch_turn()
            self.print_message()
        # ...repeat until there is a winner or tie
         # Outside the loop, render state at the end of a game
        self.render()

game_instance = Game()
game_instance.play_game()
# game_instance.render()
# game_instance.place_piece()
