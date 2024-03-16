import unittest
from texttable import Texttable
from Controller.service import Service
from Repository.repository import BoardRepository
from Domain.board import Board
from Repository.BoardRepositoryException import BoardRepoException


class BoardRepositoryServiceTest(unittest.TestCase):
    def setUp(self):
        self.board_repo = BoardRepository()
        self.service = Service(self.board_repo)
        self.width, self.height, self.is_first, a = self.board_repo.file_viewing("settings.txt")
        self.data = Board(self.width, self.height).data

    def test_file_viewing(self):
        """
        tests if the file_viewing method was executed successfully or not
        :return: None
        """
        self.assertEqual(self.board_repo.file_viewing("settings_TRUE.txt"), [6, 7, True, True])
        self.assertEqual(self.board_repo.file_viewing("settings_TRUE_3x6.txt"), [3, 6, True, True])
        self.assertEqual(self.board_repo.file_viewing("settings_FALSE.txt"), [6, 7, False, True])
        with self.assertRaises(BoardRepoException) as be:
            self.board_repo.file_viewing("settings_error_height_width.txt")
        self.assertEqual(str(be.exception), "The file height/width are invalid!")

        with self.assertRaises(BoardRepoException) as be:
            self.board_repo.file_viewing("settings_error_is_first.txt")
        self.assertEqual(str(be.exception), "The file contents are invalid!")

        with self.assertRaises(BoardRepoException) as be:
            self.board_repo.file_viewing("settings_error_index.txt")
        self.assertEqual(str(be.exception), "The file contents are invalid!")

    def test_is_over(self):
        """
        tests if the is_over method was executed successfully or not
        :return:
        """
        self.assertEqual(self.service.is_over(self.data), False)
        self.data = [['-' for _ in self.data] for _ in self.data]
        self.assertEqual(self.service.is_over(self.data), True)

    def test_move_1_X(self):
        """
        tests all the possible types of moves
        :return:
        """
        self.assertEqual(self.board_repo.move(0, 0, 'X'),
                         [['X', '-', ' ', ' ', ' ', ' '], ['-', '-', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']])

    def test_move_2_X(self):
        """
        tests all the possible types of moves
        :return:
        """
        self.assertEqual(self.board_repo.move(1, 2, 'X'),
                         [[' ', '-', '-', '-', ' ', ' '], [' ', '-', 'X', '-', ' ', ' '],
                          [' ', '-', '-', '-', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']])

    def test_move_3_X(self):
        """
        tests all the possible types of moves
        :return:
        """
        self.assertEqual(self.board_repo.move(0, 5, 'X'),
                         [[' ', ' ', ' ', ' ', '-', 'X'], [' ', ' ', ' ', ' ', '-', '-'],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']])

    def test_move_4_X(self):
        """
        tests all the possible types of moves
        :return:
        """
        self.assertEqual(self.board_repo.move(0, 2, 'X'),
                         [[' ', '-', 'X', '-', ' ', ' '], [' ', '-', '-', '-', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']])

    def test_move_5_X(self):
        """
        tests all the possible types of moves
        :return:
        """
        self.assertEqual(self.board_repo.move(6, 5, 'X'),
                         [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '-', '-'],
                          [' ', ' ', ' ', ' ', '-', 'X']])

    def test_move_6_X(self):
        """
        tests all the possible types of moves
        :return:
        """
        self.assertEqual(self.board_repo.move(6, 4, 'X'),
                         [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '-', '-', '-'],
                          [' ', ' ', ' ', '-', 'X', '-']])

    def test_move_7_X(self):
        """
        tests all the possible types of moves
        :return:
        """
        self.assertEqual(self.board_repo.move(6, 0, 'X'),
                         [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], ['-', '-', ' ', ' ', ' ', ' '],
                          ['X', '-', ' ', ' ', ' ', ' ']])

    def test_move_8_X(self):
        """
        tests all the possible types of moves
        :return:
        """
        self.assertEqual(self.board_repo.move(2, 0, 'X'),
                         [[' ', ' ', ' ', ' ', ' ', ' '], ['-', '-', ' ', ' ', ' ', ' '],
                          ['X', '-', ' ', ' ', ' ', ' '], ['-', '-', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']])

    def test_move_9_X(self):
        """
        tests all the possible types of moves
        :return:
        """
        self.assertEqual(self.board_repo.move(2, 5, 'X'),
                         [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '-', '-'],
                          [' ', ' ', ' ', ' ', '-', 'X'], [' ', ' ', ' ', ' ', '-', '-'],
                          [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ']])

    def test_move_error(self):
        """
        tests if the move method was executed successfully or not
        :return:
        """
        self.board_repo.move(1, 0, 'X')
        with self.assertRaises(BoardRepoException) as be:
            self.board_repo.move(1, 0, 'X')
        self.assertEqual(str(be.exception), "Move option is invalid!")

    def test_computer_move(self):
        """
        tests if the computer move method was executed successfully or not
        :return:
        """
        self.assertEqual(self.board_repo.computer_moves_first(),
                         (0, 0))

    def test_turn_data_into_board(self):
        """
        tests if the turn_data_into_board method was executed successfully or not
        :return:
        """
        self.assertEqual(self.service.turn_data_into_board()[0], "+")
        self.assertEqual(self.service.turn_data_into_board()[1], "-")
        self.assertEqual(self.service.turn_data_into_board()[26], "-")
        self.assertEqual(self.service.turn_data_into_board()[31], "|")

    def test_computer_moves_middle(self):
        """
        tests if the computer successfully moved to the middle of the table
        :return:
        """
        move1, move2 = self.board_repo.computer_moves_middle()
        self.assertEqual(move1, 3)
        self.assertEqual(move2, 3)

    def test_computer_moves_mirror(self):
        """
        tests if the computer successfully mirrored the last move
        :return:
        """
        self.board_repo.move(0, 0, 'X')
        move1, move2 = self.board_repo.computer_moves_mirror()
        self.assertEqual(move1, 5)
        self.assertEqual(move2, 5)

    def test_computer_moves_random(self):
        """
        tests if the computer successfully moved randomly on the board
        :return:
        """
        self.board_repo.move(0, 1, 'X')
        self.board_repo.move(2, 5, 'X')
        self.board_repo.move(0, 5, 'X')
        self.board_repo.move(2, 0, 'X')
        self.board_repo.move(2, 2, 'X')
        self.board_repo.move(4, 3, 'X')
        self.board_repo.move(5, 0, 'X')
        self.board_repo.move(5, 5, 'X')
        self.board_repo.move(6, 2, 'X')
        move1, move2 = self.board_repo.computer_moves_random()
        self.assertEqual(move1, 0)
        self.assertEqual(move2, 3)

    def test_empty_squares(self):
        """
        tests if the empty_squares function returns a list of tuples of all the squares that are empty
        :return:
        """
        self.assertEqual(self.service.empty_squares(),
                         [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                          (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3),
                          (3, 4), (3, 5), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 0), (5, 1), (5, 2),
                          (5, 3), (5, 4), (5, 5), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
        pass

    def test_can_computer_win(self):
        """
        it tests if the computer can win in 1 move
        :return:
        """
        m1, m2 = self.service.can_computer_win()
        self.assertEqual(m1, False)
        self.assertEqual(m2, False)
        self.board_repo.move(1, 2, 'X')
        self.board_repo.move(0, 4, 'X')
        self.board_repo.move(2, 5, 'X')
        self.board_repo.move(2, 0, 'X')
        self.board_repo.move(4, 2, 'X')
        self.board_repo.move(5, 5, 'X')
        self.board_repo.move(6, 1, 'X')
        self.board_repo.move(6, 3, 'X')
        self.board_repo.move(0, 0, 'X')
        move1, move2 = self.service.can_computer_win()
        self.assertEqual(move1, 4)
        self.assertEqual(move2, 0)
        pass


class BoardTest(unittest.TestCase):
    def test_domain(self):
        """
        tests the whole Board (domain) class
        :return:
        """
        table = Texttable()
        for _ in range(2):
            table.add_row([' '] * 2)
        self.assertEqual(str(Board(2, 2)), table.draw())


class BoardExceptionTest(unittest.TestCase):
    def test_exception(self):
        """
        tests the whole BoardException class
        :return:
        """
        self.assertEqual(BoardRepoException("Invalid").message, "Invalid")
        self.assertEqual(str(BoardRepoException("Invalid").message), "Invalid")
