import sudoku
import ui

def main_start_game():
    choose = input("Select you play-style: \n Input 1 for oldschool insertion through Terminal Window. \n Input 2 for sophisticated UI and Keyboard insertion. \n")
    while choose != "1" and choose != "2": 
            choose = input("Incorect selection, please choose 1 or 2 again:  ")
    if choose == "1":
        sudoku.start_game()
    elif choose == "2":
        ui.start_game()

main_start_game()