from Controller.service import Service
from Domain.board import Board
from Repository.repository import BoardRepository
from Repository.BoardRepositoryException import BoardRepoException
import PySimpleGUI as Sg


class UI:
    def __init__(self):
        self.board_repo = BoardRepository()
        self.service = Service(self.board_repo)
        try:
            x = self.board_repo.file_viewing("settings.txt")
        except BoardRepoException as be:
            print(be)
            return
        except ValueError:
            print("Invalid move option!")
            return
        if x[-1] is False:
            self.start_normal_ui()
        else:
            self.start_gui()

    @staticmethod
    def you_lost():
        print("Computer wins!")
        print()

    @staticmethod
    def you_won():
        print("Player wins!")
        print()

    def start_normal_ui(self):
        if self.board_repo.is_first is True:
            print(self.service.turn_data_into_board())
            while True:
                move_option = input("Enter your move, or exit: ")
                try:
                    if move_option == 'exit':
                        return
                    else:
                        move_option_split = move_option.split()
                        if len(move_option_split) != 2:
                            raise BoardRepoException("Invalid move option!")
                        elif move_option[2] == ' ':
                            raise BoardRepoException("Invalid move option!")
                        else:
                            try:
                                if int(move_option_split[0]) >= self.board_repo.height:
                                    raise BoardRepoException("Invalid move option!")
                                if int(move_option_split[1]) >= self.board_repo.width:
                                    raise BoardRepoException("Invalid move option!")
                            except ValueError:
                                raise BoardRepoException("Invalid move option!")
                except BoardRepoException as be:
                    print(be)
                else:
                    break
            self.board_repo.move(int(move_option[0]), int(move_option[2]), 'X')
            computer_turn = True
        else:
            if self.board_repo.width % 2 == 1 and self.board_repo.height % 2 == 1:
                move_1, move_2 = self.board_repo.computer_moves_middle()
                print(f"Computer moved {move_1},{move_2}")
            else:
                move_1, move_2 = self.board_repo.computer_moves_random()
                print(f"Computer moved {move_1},{move_2}")
            computer_turn = False
        while True:
            print(self.service.turn_data_into_board())
            if self.service.is_over(self.board_repo.data) is False and computer_turn is False:
                while True:
                    move_option = input("Enter your move, or exit: ")
                    try:
                        if move_option == 'exit':
                            return
                        else:
                            move_option_split = move_option.split()
                            if len(move_option_split) != 2:
                                raise BoardRepoException("Invalid move option!")
                            elif move_option[2] == ' ':
                                raise BoardRepoException("Invalid move option!")
                            else:
                                try:
                                    if int(move_option_split[0]) >= self.board_repo.height:
                                        raise BoardRepoException("Invalid move option!")
                                    if int(move_option_split[1]) >= self.board_repo.width:
                                        raise BoardRepoException("Invalid move option!")
                                except ValueError:
                                    raise BoardRepoException("Invalid move option!")
                        self.board_repo.move(int(move_option[0]), int(move_option[2]), 'X')
                    except BoardRepoException as be:
                        print(be)
                    else:
                        break
                print()
                computer_turn = True
            elif self.service.is_over(self.board_repo.data) is False and computer_turn is True:
                move_1, move_2 = self.service.can_computer_win()
                if move_1 is not False and move_2 is not False:
                    self.board_repo.move(move_1, move_2, 'O')
                    print(f"Computer moved {move_1},{move_2}")
                elif self.board_repo.width % 2 == 1 and self.board_repo.height % 2 == 1 and self.board_repo.is_first is False:
                    move_1, move_2 = self.board_repo.computer_moves_mirror()
                    print(f"Computer moved {move_1},{move_2}")
                else:
                    move_1, move_2 = self.board_repo.computer_moves_random()
                    print(f"Computer moved {move_1},{move_2}")
                computer_turn = False
            elif self.service.is_over(self.board_repo.data) is True:
                print("Game over!")
                if computer_turn is True:
                    self.you_won()
                else:
                    self.you_lost()
                return

    def start_gui(self):
        window = self.gui_board_initialize()
        while True:
            computer_turn = not self.board_repo.is_first
            event, values = window.read()
            if event == "Exit" or event == Sg.WINDOW_CLOSED:
                break
            elif event == "Start":
                window_board, board = self.gui_board_create()
                self.board_repo.data = Board(self.board_repo.width, self.board_repo.height).data
                self.board_repo.mirror_X = []
                if computer_turn is True and self.board_repo.height % 2 != 0 and self.board_repo.width % 2 != 0:
                    middle, move_mirror = True, True
                else:
                    middle, move_mirror = False, False
                while True:
                    event, values = window_board.read()
                    self.gui_board_update(window_board)
                    if self.service.is_over(self.board_repo.data) is True:
                        if computer_turn:
                            self.you_won()
                        else:
                            self.you_lost()
                        break
                    elif computer_turn is True:
                        if event == "Back" or event == Sg.WINDOW_CLOSED:
                            print(self.board_repo.data)
                            break
                        if middle is True:
                            move1, move2 = self.board_repo.computer_moves_middle()
                            self.gui_board_update(window_board)
                            print(f"Computer moved {move1},{move2}")
                            middle = False
                        elif move_mirror is True:
                            move1, move2 = self.board_repo.computer_moves_mirror()
                            self.gui_board_update(window_board)
                            print(f"Computer moved {move1},{move2}")
                        else:
                            move1, move2 = self.service.can_computer_win()
                            if move1 is not False:
                                self.board_repo.move(move1, move2, "O")
                            else:
                                move1, move2 = self.board_repo.computer_moves_random()
                            self.gui_board_update(window_board)
                            print(f"Computer moved {move1},{move2}")
                        computer_turn = not computer_turn
                    elif computer_turn is False:
                        if event == "Back" or event == Sg.WINDOW_CLOSED:
                            break
                        elif event != "Start":
                            try:
                                x = int(event[2])
                                y = int(event[5])
                                self.board_repo.move(x, y, "X")
                                self.gui_board_update(window_board)
                            except ValueError:
                                self.board_repo.move(0, 0, "X")
                                self.gui_board_update(window_board)
                        computer_turn = not computer_turn
                window_board.close()
        window.close()

    def gui_board_create(self):
        # x = self.board_repo.width  # width
        # y = self.board_repo.height  # height
        board = [[] for _ in range(self.board_repo.height + 1)]
        for i in range(self.board_repo.height + 1):
            for j in range(self.board_repo.width + 1):
                if i == 0 and j == 0:
                    board[0].append(
                        Sg.Button("||", disabled=True, size=(5, 3), border_width=2, font="bold 10"))
                elif i == 0 and j != 0:
                    board[0].append(
                        Sg.Button(f"{j - 1}", disabled=True, size=(5, 3), border_width=2, font="bold 10"))
                elif i != 0 and j == 0:
                    board[i].append(
                        Sg.Button(f"{i - 1}", disabled=True, size=(5, 3), border_width=2, font="bold 10"))
                else:
                    board[i].append(
                        Sg.Button(" ", size=(5, 3), border_width=2, key=f"-{i - 1, j - 1}-", font="bold 10"))
        layout_board = [
            [Sg.Button("Start", font="normal 15", border_width=2),
             Sg.Button("Back", font="normal 15", border_width=2)],
            board
        ]
        window_board = Sg.Window("Board", layout_board,
                                 size=(90 * self.board_repo.width, 73 * (self.board_repo.height + 1)),
                                 element_justification='c',
                                 grab_anywhere=True,
                                 no_titlebar=False, background_color='Grey')
        return window_board, board

    def gui_board_update(self, window_board):
        for i in range(self.board_repo.height):
            for j in range(self.board_repo.width):
                if self.board_repo.data[i][j] != ' ':
                    window_board[f"-{i, j}-"].update(self.board_repo.data[i][j], disabled=True)

    @staticmethod
    def gui_board_initialize():
        Sg.theme("Dark Amber")
        layout = [
            [
                Sg.Text("Welcome to Obstruction!", font="rockwell 45")
            ],
            [
                Sg.Image(source="Obstruction.png", pad=(100, 80))
            ],
            [
                Sg.Button("Start", size=(20, 2), font="normal 14")
            ],
            [
                Sg.Button("Exit", size=(20, 2), font="normal 14")
            ]
        ]
        window = Sg.Window("Obstruction", layout, size=(1000, 654), element_justification='c', no_titlebar=False,
                           grab_anywhere=True)
        return window


a = UI()
