from Domain.board import Board
from Repository.BoardRepositoryException import BoardRepoException
import random


class BoardRepository:
    def __init__(self):
        self.data = []  # board list
        self.width = 0  # int
        self.height = 0  # int
        self.is_first = False
        self.mirror_X = []

    def file_viewing(self, file):
        """
        this method opens the file "settings.txt" and it takes the width, height from there
        :param file: name of the file
        :return: a list of the values that it took from the file ( used for testing )
        """
        with open(file, 'r') as file:
            file_line = file.readline()
            file_line = file_line.split()
            try:
                if file_line[3].casefold() == '6x6' or file_line[3].casefold() == '6x7' or \
                        file_line[3].casefold() == '7x7' or file_line[3].casefold() == '3x6':
                    self.width = int(file_line[3][0])
                    self.height = int(file_line[3][-1])
                    file_line = file.readline()
                    file_line = file_line.split()
                    if file_line[6].casefold() == 'yes':
                        self.is_first = True
                        self.data, self.width, self.height = Board(self.width,
                                                                   self.height).data, self.width, self.height
                        file_line = file.readline()
                        file_line = file_line.split()
                        if file_line[7].casefold() == "yes":
                            return [self.width, self.height, self.is_first, True]
                        elif file_line[7].casefold() == "no":
                            return [self.width, self.height, self.is_first, False]
                        else:
                            raise BoardRepoException("The file contents are invalid!")
                    elif file_line[6].casefold() == 'no':
                        self.is_first = False
                        self.data, self.width, self.height = Board(self.width,
                                                                   self.height).data, self.width, self.height
                        file_line = file.readline()
                        file_line = file_line.split()
                        if file_line[7].casefold() == "yes":
                            return [self.width, self.height, self.is_first, True]
                        elif file_line[7].casefold() == "no":
                            return [self.width, self.height, self.is_first, False]
                        else:
                            raise BoardRepoException("The file contents are invalid!")
                    else:
                        raise BoardRepoException("The file contents are invalid!")
                else:
                    raise BoardRepoException("The file height/width are invalid!")
            except IndexError:
                raise BoardRepoException("The file contents are invalid!")

    def move(self, width, height, symbol):
        """
        Moves the symbol (X or O) at a certain location
        :param width: the width
        :param height: the height
        :param symbol: the symbol
        :return: the data list if the move is successful, also used for testing
        """
        #  print(self.data)
        if self.data[width][height] == " ":
            self.data[width][height] = symbol
            if width != 0 and width != self.height - 1 and height != 0 and height != self.width - 1:
                self.data[width - 1][height - 1] = '-'
                self.data[width][height - 1] = '-'
                self.data[width + 1][height - 1] = '-'
                self.data[width + 1][height] = '-'
                self.data[width - 1][height] = '-'
                self.data[width - 1][height + 1] = '-'
                self.data[width][height + 1] = '-'
                self.data[width + 1][height + 1] = '-'
            elif width == 0 and height == 0:
                self.data[width][height + 1] = '-'
                self.data[width + 1][height] = '-'
                self.data[width + 1][height + 1] = '-'
            elif width == 0 and height != self.width - 1:
                self.data[width][height - 1] = '-'
                self.data[width][height + 1] = '-'
                self.data[width + 1][height] = '-'
                self.data[width + 1][height + 1] = '-'
                self.data[width + 1][height - 1] = '-'
            elif width == 0 and height == self.width - 1:
                self.data[width][height - 1] = '-'
                self.data[width + 1][height - 1] = '-'
                self.data[width + 1][height] = '-'
            elif width == self.height - 1 and height == 0:
                self.data[width - 1][height + 1] = '-'
                self.data[width - 1][height] = '-'
                self.data[width][height + 1] = '-'
            elif width == self.height - 1 and height != self.width - 1:
                self.data[width][height - 1] = '-'
                self.data[width][height + 1] = '-'
                self.data[width - 1][height] = '-'
                self.data[width - 1][height + 1] = '-'
                self.data[width - 1][height - 1] = '-'
            elif width == self.height - 1 and height == self.width - 1:
                self.data[width][height - 1] = '-'
                self.data[width - 1][height - 1] = '-'
                self.data[width - 1][height] = '-'
            elif width != 0 and width != self.height - 1 and height == 0:
                self.data[width - 1][height] = '-'
                self.data[width - 1][height + 1] = '-'
                self.data[width][height + 1] = '-'
                self.data[width + 1][height] = '-'
                self.data[width + 1][height + 1] = '-'
            elif width != 0 and width != self.height - 1 and height == self.width - 1:
                self.data[width][height - 1] = '-'
                self.data[width - 1][height - 1] = '-'
                self.data[width - 1][height] = '-'
                self.data[width + 1][height - 1] = '-'
                self.data[width + 1][height] = '-'
        else:
            raise BoardRepoException("Move option is invalid!")
        return self.data

    def computer_moves_first(self):
        """
        method that makes the computer move on the first open square
        :return: the width and height where the computer moved, used for testing and printing
        """
        for i in range(self.height):
            for j in range(self.width):
                if self.data[i][j] == ' ':
                    self.move(i, j, 'O')
                    return i, j

    def computer_moves_random(self):
        while True:
            i = random.randint(0, self.height - 1)
            j = random.randint(0, self.width - 1)
            if self.data[i][j] == ' ':
                self.move(i, j, 'O')
                return i, j

    def computer_moves_mirror(self):
        """
        method that makes the computer mirror the previous move (the player's)
        :return: x and y of the move
        """
        for i in range(self.height):
            for j in range(self.width):
                if self.data[i][j] == "X" and [i, j] not in self.mirror_X:
                    self.mirror_X.append([i, j])
                    self.move(self.width - i - 1, self.width - j - 1, 'O')
                    return self.width - i - 1, self.width - j - 1

    def computer_moves_middle(self):
        self.move(self.height // 2, self.width // 2, 'O')
        return self.height // 2, self.width // 2
