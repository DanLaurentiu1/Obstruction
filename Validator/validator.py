from Controller.service import Service
from Repository.repository import BoardRepository, BoardRepoException


class Validate:
    def __init__(self):
        pass

    @staticmethod
    def validate_file_viewing(function_name):
        try:
            function_name("settings.txt")
            return False
        except BoardRepoException as be:
            print(be)
            return True
