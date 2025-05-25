import os
import time
from colorama import init, Fore, Style
import sys

# Initialize Colorama
init(autoreset=True)

# Optional: clear terminal for better UI
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for animated text output
def animated_text(text, color=Fore.WHITE, delay=0.05):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to save question to file
def save_question_to_file(file_name, question_data):
    with open(file_name, 'a') as file:
        file.write(f"QUESTION: {question_data['question']}\n")
        file.write(f"A. {question_data['a']}\n")
        file.write(f"B. {question_data['b']}\n")
        file.write(f"C. {question_data['c']}\n")
        file.write(f"D. {question_data['d']}\n")
        file.write(f"ANSWER: {question_data['answer'].upper()}\n")
        file.write("---\n")

# Function to view all questions
def view_all_questions(file_name):
    if not os.path.exists(file_name):
        print(Fore.RED + "No questions found! Please add questions first.")
        return
    with open(file_name, 'r') as file:
        print(Fore.GREEN + file.read())

# Function to remove a question (basic version that just removes the last question)
def remove_last_question(file_name):
    if not os.path.exists(file_name):
        print(Fore.RED + "No questions to remove!")
        return
    with open(file_name, 'r') as file:
        lines = file.readlines()
    if len(lines) < 7:
        print(Fore.RED + "❌ Not enough data to remove a question.")
        return
    with open(file_name, 'w') as file:
        file.writelines(lines[:-7])
    print(Fore.GREEN + "✅ Last question removed successfully!")

# Display "QUIZ" ASCII Art for flair
def print_ascii_art():
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

# Function to add a new question
def add_question(file_name):
    while True:
        clear()
        animated_text("💭 Enter your question:", Fore.WHITE, 0.1)
        question = input(f"{Style.BRIGHT}{Fore.GREEN}Your Question: {Style.RESET_ALL}").strip()

        animated_text(" • Enter Option A:", Fore.YELLOW, 0.1)
        a = input(f"{Style.BRIGHT}{Fore.CYAN}Option A: {Style.RESET_ALL}").strip()

        animated_text(" • Enter Option B:", Fore.YELLOW, 0.1)
        b = input(f"{Style.BRIGHT}{Fore.CYAN}Option B: {Style.RESET_ALL}").strip()

        animated_text(" • Enter Option C:", Fore.YELLOW, 0.1)
        c = input(f"{Style.BRIGHT}{Fore.CYAN}Option C: {Style.RESET_ALL}").strip()

        animated_text(" • Enter Option D:", Fore.YELLOW, 0.1)
        d = input(f"{Style.BRIGHT}{Fore.CYAN}Option D: {Style.RESET_ALL}").strip()

        while True:
            animated_text("✅ Enter the correct answer (A/B/C/D):", Fore.GREEN, 0.1)
            answer = input(f"{Style.BRIGHT}{Fore.WHITE}Answer: {Style.RESET_ALL}").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print(Fore.RED + "❌ Invalid choice. Please enter A, B, C, or D.")

        question_data = {
            'question': question,
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'answer': answer
        }

        save_question_to_file(file_name, question_data)
        animated_text("✅ Question saved successfully!", Fore.GREEN, 0.1)

        again = input(Fore.CYAN + "➕ Add another question? Enter 1 to continue or 4 to stop: ").strip()
        if again == '4':
            animated_text("\n🚀 Quiz creation finished!", Fore.MAGENTA, 0.1)
            print(f"{Style.BRIGHT}{Fore.YELLOW}{file_name}{Style.RESET_ALL}")
            animated_text("\n📄 Showing all saved questions...\n", Fore.LIGHTWHITE_EX, 0.08)
            view_all_questions(file_name)
            input("\nPress Enter to return to the main menu...")
            break     

# Function to display the main menu and handle user choices
def main_menu():
    file_name = "quiz_data.txt"

    while True:
        clear()
        print_ascii_art()
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n📚 Welcome to the Quiz Creator!")
        print(Fore.LIGHTWHITE_EX + "💡 Create your own quiz questions and answers effortlessly with this program!")
        print(Fore.LIGHTMAGENTA_EX + "\nWhat would you like to do?")

        print(f"{Fore.GREEN}1. {Fore.RESET}Add a question")
        print(f"{Fore.CYAN}2. {Fore.RESET}Remove a question")
        print(f"{Fore.YELLOW}3. {Fore.RESET}View all questions")
        print(f"{Fore.RED}4. {Fore.RESET}Exit")

        user_choice = input(Fore.LIGHTMAGENTA_EX + "\nPick an option (1/2/3/4): ").strip()

        if user_choice == '1':
            add_question(file_name)
        elif user_choice == '2':
            remove_last_question(file_name)
            input("\nPress Enter to return to menu...")
        elif user_choice == '3':
            view_all_questions(file_name)
            input("\nPress Enter to return to menu...")
        elif user_choice == '4':
            animated_text("\n🚀 Exiting the program. See you soon!", Fore.MAGENTA, 0.1)
            sys.exit()
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()