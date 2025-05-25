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

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def animated_text(self, text, color=Fore.WHITE, delay=0.05):
        for char in text:
            print(color + char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def print_ascii_art(self):
        print(Fore.MAGENTA + """
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |    ___       | || | _____  _____ | || |     _____    | || |   ________   | |
| |  .'   '.     | || ||_   _||_   _|| || |    |_   _|   | || |  |  __   _|  | |
| | /  .-.  \    | || |  | |    | |  | || |      | |     | || |  |_/  / /    | |
| | | |   | |    | || |  | '    ' |  | || |      | |     | || |     .'.' _   | |
| | \  `-'  \_   | || |   \ `--' /   | || |     _| |_    | || |   _/ /__/ |  | |
| |  `.___.\__|  | || |    `.__.'    | || |    |_____|   | || |  |________|  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
        """)
        time.sleep(1)

    def main_menu(self):
        while True:
            self.clear_screen()
            self.print_ascii_art()
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n📚 Welcome to the Quiz App!")
            print(Fore.LIGHTWHITE_EX + "💡 Choose whether to create or take a quiz!\n")
            print(f"{Fore.GREEN}1. {Fore.RESET}Create a Quiz")
            print(f"{Fore.CYAN}2. {Fore.RESET}Take a Quiz")
            print(f"{Fore.RED}3. {Fore.RESET}Exit")

            choice = input(Fore.LIGHTMAGENTA_EX + "\nPick an option (1/2/3): ").strip()

            if choice == '1':
                self.creator.main_menu()
            elif choice == '2':
                self.reader.launch_quiz()
            elif choice == '3':
                self.animated_text("\n🚀 Exiting the program. See you soon!", Fore.MAGENTA, 0.1)
                sys.exit()
            else:
                print(Fore.RED + "❌ Invalid choice. Please try again.")
                time.sleep(1)