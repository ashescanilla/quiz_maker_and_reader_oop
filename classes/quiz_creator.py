import os
import time
from colorama import init, Fore, Style
import sys

# Initialize Colorama
init(autoreset=True)

class QuizCreator:
    def __init__(self, file_name = "quiz_data.txt"):
        self.file_name = file_name
    
    # Optional: clear terminal for better UI
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Function for animated text output
    def animated_text(self, text, color=Fore.WHITE, delay=0.05):
        for char in text:
            print(color + char, end='', flush=True)
            time.sleep(delay)
        print()

    # Function to save question to file
    def save_question_to_file(self, question_data):
        with open(self.file_name, 'a') as file:
            file.write(f"QUESTION: {question_data['question']}\n")
            file.write(f"A. {question_data['a']}\n")
            file.write(f"B. {question_data['b']}\n")
            file.write(f"C. {question_data['c']}\n")
            file.write(f"D. {question_data['d']}\n")
            file.write(f"ANSWER: {question_data['answer'].upper()}\n")
            file.write("---\n")

    # Function to view all questions
    def view_all_questions(self):
        if not os.path.exists(self.file_name):
            print(Fore.RED + "No questions found! Please add questions first.")
            return
        with open(self.file_name, 'r') as file:
            print(Fore.GREEN + file.read())

    # Function to remove a question (basic version that just removes the last question)
    def remove_last_question(self):
        if not os.path.exists(self.file_name):
            print(Fore.RED + "No questions to remove!")
            return
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
        if len(lines) < 7:
            print(Fore.RED + "❌ Not enough data to remove a question.")
            return
        with open(self.file_name, 'w') as file:
            file.writelines(lines[:-7])
        print(Fore.GREEN + "✅ Last question removed successfully!")

    # Function to add a new question
    def add_question(self):
        while True:
            self.clear()
            self.animated_text("💭 Enter your question:", Fore.WHITE, 0.1)
            question = input(f"{Style.BRIGHT}{Fore.GREEN}Your Question: {Style.RESET_ALL}").strip()

            self.animated_text(" • Enter Option A:", Fore.YELLOW, 0.1)
            option_a = input(f"{Style.BRIGHT}{Fore.CYAN}Option A: {Style.RESET_ALL}").strip()

            self.animated_text(" • Enter Option B:", Fore.YELLOW, 0.1)
            option_b = input(f"{Style.BRIGHT}{Fore.CYAN}Option B: {Style.RESET_ALL}").strip()

            self.animated_text(" • Enter Option C:", Fore.YELLOW, 0.1)
            option_c = input(f"{Style.BRIGHT}{Fore.CYAN}Option C: {Style.RESET_ALL}").strip()

            self.animated_text(" • Enter Option D:", Fore.YELLOW, 0.1)
            option_d = input(f"{Style.BRIGHT}{Fore.CYAN}Option D: {Style.RESET_ALL}").strip()

            while True:
                self.animated_text("✅ Enter the correct answer (A/B/C/D):", Fore.GREEN, 0.1)
                answer = input(f"{Style.BRIGHT}{Fore.WHITE}Answer: {Style.RESET_ALL}").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print(Fore.RED + "❌ Invalid choice. Please enter A, B, C, or D.")

            question_data = {
                'question': question,
                'a': option_a,
                'b': option_b,
                'c': option_c,
                'd': option_d,
                'answer': answer
            }

            self.save_question_to_file(question_data)
            self.animated_text("✅ Question saved successfully!", Fore.GREEN, 0.1)

            again = input(Fore.CYAN + "➕ Add another question? Enter 1 to continue or 4 to stop: ").strip()
            if again == '4':
                self.animated_text("\n🚀 Quiz creation finished!", Fore.MAGENTA, 0.1)
                print(f"{Style.BRIGHT}{Fore.YELLOW}{self.file_name}{Style.RESET_ALL}")
                self.animated_text("\n📄 Showing all saved questions...\n", Fore.LIGHTWHITE_EX, 0.08)
                self.view_all_questions()
                input("\nPress Enter to return to the main menu...")
                break     

    # Function to display the main menu and handle user choices
    def main_menu(self):
        while True:
            self.clear()
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n📚 Welcome to the Quiz Creator!")
            print(Fore.LIGHTWHITE_EX + "💡 Create your own quiz questions and answers effortlessly with this program!")
            print(Fore.LIGHTMAGENTA_EX + "\nWhat would you like to do?")

            print(f"{Fore.GREEN}1. {Fore.RESET}Add a question")
            print(f"{Fore.CYAN}2. {Fore.RESET}Remove a question")
            print(f"{Fore.YELLOW}3. {Fore.RESET}View all questions")
            print(f"{Fore.RED}4. {Fore.RESET}Exit")

            user_choice = input(Fore.LIGHTMAGENTA_EX + "\nPick an option (1/2/3/4): ").strip()

            if user_choice == '1':
                self.add_question()
            elif user_choice == '2':
                self.remove_last_question()
                input("\nPress Enter to return to menu...")
            elif user_choice == '3':
                self.view_all_questions()
                input("\nPress Enter to return to menu...")
            elif user_choice == '4':
                self.animated_text("\n🚀 Exiting the program. See you soon!", Fore.MAGENTA, 0.1)
                break
            else:
                print(Fore.RED + "❌ Invalid choice. Please try again.")
                time.sleep(1)