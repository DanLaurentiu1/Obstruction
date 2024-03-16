from texttable import Texttable


class Service:
    def __init__(self, board_repo):
        self.b_r = board_repo

    def is_over(self, data):
        """
        method shows if the game is over or not
        :param data: False is not the game is over
        :return: True is the game is over
        """
        for i in range(self.b_r.height):
            for j in range(self.b_r.width):
                if data[i][j] == ' ':
                    return False
        return True

    def turn_data_into_board(self):
        """
        this method turns the data list into an actual table
        :return: the table, used for testing and also for printing
        """
        table = Texttable()
        header_row_oriz = ['||']
        for i in range(len(self.b_r.data[0])):
            header_row_oriz.append(i)
        table.header(header_row_oriz)
        table.set_cols_align(['c'] * (self.b_r.width + 1))
        for i in range(self.b_r.height):
            table.add_row([i] + [x for x in self.b_r.data[i]])
        return table.draw()

    def can_computer_win(self):
        """
        it looks if the computer can win in one move:
        we have the list moves which is a list of 9 different lists
        each number (from 0 to 8) represents a move that covers exactly that amount of squares
                -> moves[6] will have the x and y of all the possible moves that can cover 6 squares
        if the board has a number of empty squares < 10 means that MAYBE there is a move that can cover all the remaining squares
        if that is true, it returns the x and y of the FIRST move that can cover all the remaining squares
        :return: the x and y of the FIRST move that can cover all the remaining squares
        """
        board = self.b_r.data
        moves = [[] for _ in range(9)]
        empty_squares = self.empty_squares()
        for move in empty_squares:
            count = 0
            if move[0] - 1 >= 0 and move[1] - 1 >= 0 and board[move[0] - 1][move[1] - 1] == ' ':
                count = count + 1
            if move[0] - 1 >= 0 and board[move[0] - 1][move[1]] == ' ':
                count = count + 1
            if move[0] - 1 >= 0 and move[1] + 1 < self.b_r.width and board[move[0] - 1][move[1] + 1] == ' ':
                count = count + 1
            if move[1] + 1 < self.b_r.width and board[move[0]][move[1] + 1] == ' ':
                count = count + 1
            if move[0] + 1 < self.b_r.height and move[1] + 1 < self.b_r.width and \
                    board[move[0] + 1][move[1] + 1] == ' ':
                count = count + 1
            if move[0] + 1 < self.b_r.height and board[move[0] + 1][move[1]] == ' ':
                count = count + 1
            if move[0] + 1 < self.b_r.height and move[1] - 1 >= 0 and board[move[0] + 1][move[1] - 1] == ' ':
                count = count + 1
            if move[1] - 1 >= 0 and board[move[0]][move[1] - 1] == ' ':
                count = count + 1
            moves[count].append(move)
        empty = len(empty_squares)
        if empty <= 9:
            if len(moves[empty - 1]) > 0:
                return moves[empty - 1][0][0], moves[empty - 1][0][1]
            return False, False
        return False, False

    def empty_squares(self):
        """
        :return: the x and y of all the empty squares ( a list of tuples )
        """
        result = []
        for i in range(self.b_r.height):
            for j in range(self.b_r.width):
                if self.b_r.data[i][j] == " ":
                    result.append((i, j))
        return result
