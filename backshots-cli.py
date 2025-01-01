from InquirerPy import inquirer as inq
from InquirerPy.separator import Separator as sep
import os, time


# Clear the terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Main class
class backshots:
    # Initialize the class
    def __init__(self):
        clear()
        run = inq.confirm(message="Run Backshots?").execute()
        if run:
            self.running = True
            self.main_loop()
        else:
            clear()
            print("Exiting...")
            time.sleep(0.5)
            exit(0)

    # Main menu
    def menu(self):
        clear()
        print("-" * 50)
        print("Backshots CLI")
        print("-" * 50)
        options = [
            {"value": "new_round", "name": "New Round"},
            sep(),
            {"value": "exit", "name": "Exit"},
        ]
        choice = inq.select(
            message="Please Select an Option", choices=options, qmark="🎯", amark="🎯"
        ).execute()
        if choice == "new_round":
            self.new_round()
        elif choice == "exit":
            self.running = False

    # New round
    def new_round(self):
        clear()
        live = int(
            inq.number(
                message="Live Rounds",
                min_allowed=1,
                max_allowed=8,
                qmark="🔴",
                amark="🔴",
            ).execute()
        )
        blank = int(
            inq.number(
                message="Blank Rounds",
                min_allowed=1,
                max_allowed=8,
                qmark="🔵",
                amark="🔵",
            ).execute()
        )

        total = live + blank

        while total != 0:
            clear()
            probability = round((live / total * 100), 2)
            print("-" * 50)
            print(f"🔴 Live: {live} | 🔵 Blank: {blank} | Probability: {probability}%")
            print("-" * 50)
            choices = [
                {"value": "live", "name": "🔴 Live"},
                {"value": "blank", "name": "🔵 Blank"},
                sep(),
                {"value": "exit", "name": "Exit"},
            ]
            if live == 0:
                choices.pop(0)
            elif blank == 0:
                choices.pop(1)

            choice = inq.select(
                message="What type of round?", choices=choices, qmark="🎯", amark="🎯"
            ).execute()
            if choice == "live":
                live -= 1
            elif choice == "blank":
                blank -= 1
            elif choice == "exit":
                break

            total = live + blank

        print("\nRound Over\n")
        time.sleep(2)

    # Main loop
    def main_loop(self):
        while self.running:
            self.menu()

        clear()
        print("\nExiting...")
        time.sleep(0.5)
        exit(0)


# Run the class
if __name__ == "__main__":
    try:
        backshots()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
