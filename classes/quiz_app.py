from classes.quiz_creator import QuizCreator
from classes.quiz_reader import QuizReader
import os
import sys
from colorama import init, Fore, Style
import time

init(autoreset=True)

class QuizApp:
    def __init__(self, file_name = "quiz_data.txt"):
        self.file_name = file_name
        self.creator = QuizCreator(self.file_name)
        self.reader = QuizReader(self.file_name)