def main():
    """This is where all my functions will be called"""
    print("\nWELCOME TO THE GAME\n")
    print("Love is a game of tic-tac-toe, Constantly waiting for the next x or o. — Lang Leav\n")
    again = "yes"
    while again.lower() == "yes":
        current_list = [1,2,3,4,5,6,7,8,9]
        nextturn = "x"
        
        player1 = input("Player X, Please enter your name: ")
        player2 = input("Player O, Please enter your name: ")

        play_count = 0
        stop_play_on = False
        while play_count < 10 and not stop_play_on: 

            if play_count == 9:
                print("Its a Draw!!!")
                break
            
            board(current_list)
            update = int(input(f"{player1} please use enter number from 1-9: "))
            current_list = update_current_list(current_list, update, nextturn)
            board(current_list)
            nextturn = next_turn(nextturn)
            stop_play_on = check_winner(current_list, player1, player2)

            if stop_play_on:
                print(f"{player1} Wins!!!")
                break

            play_count = play_count + 1

            if play_count == 9:
                print("Its a Draw!!!")
                break

            board(current_list)
            update = int(input(f"{player2} please use enter number from 1-9: "))
            current_list = update_current_list(current_list, update, nextturn)
            board(current_list)
            nextturn = next_turn(nextturn)
            stop_play_on = check_winner(current_list, player1, player2)

            if stop_play_on:
                print(f"{player2} Wins!!!")
                break

            play_count = play_count + 1

            if play_count == 9:
                print("Its a Draw!!!")
                break
        again = input("\nWould you like to play again? yes/no: ")
        print()
    print("\nThat was fun, have a good day!\n")


def next_turn(nextturn):
    """This function will be the one changing the X's and the O's"""
    if nextturn.lower() == "x":
        nextturn = "o"
    elif nextturn.lower() == "o":
        nextturn = "x"
    return nextturn

def update_current_list(current_list, update, nextturn):
    """This function is for updating the array thats being used for the game"""
    
    if int(current_list[update - 1]) < 10:
        current_list[update - 1] = nextturn
    return current_list

def check_winner(current_list, player1, player2):
    """This function checks the array of replaced numbers to see if there is any winner or if its a draw"""
        
    if current_list[0] == current_list[1] and current_list[1] == current_list[2]:
        return True

    elif current_list[3] == current_list[4] and current_list[4] == current_list[5]:
        return True

    elif current_list[6] == current_list[7] and current_list[7] == current_list[8]:
        return True

    elif current_list[0] == current_list[3] and current_list[3] == current_list[6]:
        return True

    elif current_list[1] == current_list[4] and current_list[4] == current_list[7]:
        return True

    elif current_list[2] == current_list[5] and current_list[5] == current_list[8]:
        return True

    elif current_list[0] == current_list[4] and current_list[4] == current_list[8]:
        return True

    elif current_list[2] == current_list[4] and current_list[4] == current_list[6]:
        return True

    else:
        pass


def board(current_list):
    """This function takes the latest array and prints the board when called"""
    a = current_list[0]
    b = current_list[1]
    c = current_list[2]
    d = current_list[3]
    e = current_list[4]
    f = current_list[5]
    g = current_list[6]
    h = current_list[7]
    i = current_list[8]

    print()
    print(f"{a} | {b} | {c}")
    print(f"--+---+---")
    print(f"{d} | {e} | {f}")
    print(f"--+---+---")
    print(f"{g} | {h} | {i}")
    print()

if __name__ == "__main__":
    main()
  