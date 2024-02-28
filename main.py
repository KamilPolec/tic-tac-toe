game = True

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

round = 1
player = "O"

print("""
 _   _      _             _             
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ 
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|                                 
""")


def change_board():
    board2 = (f"""
          |     |     
       {board[0]}  |  {board[1]}  |  {board[2]}  
     _____|_____|_____
          |     |     
       {board[3]}  |  {board[4]}  |  {board[5]}  
     _____|_____|_____
          |     |     
       {board[6]}  |  {board[7]}  |  {board[8]}  
          |     |   
    """)
    print(board2)


while game:

    change_board()

    if player == "O":
        player = "X"
    else:
        player = "O"

    print(f"round: {round}")

    if not round == 10:
        to_replace = input(f"{player}'s move. Place your mark. Numbers 1-9 only. ")
        if not board[int(to_replace) - 1] == "X" and not board[int(to_replace) - 1] == "O":
            board[int(to_replace) - 1] = board[int(to_replace) - 1].replace(board[int(to_replace) - 1], player)

        else:
            print("invalid move")
            round -= 1
            if player == "X":
                player = "O"
            else:
                player = "X"
    else:
        print("It's a draw")
        break

    if round >= 3:
        for space in range(0, 3):
            if board[space] == player and board[space + 3] == player and board[space + 6] == player:
                print(f"{player} wins, Diagonal")
                change_board()
                game = False
                break

        for space in range(0, len(board), 3):
            if board[space] == player and board[space + 1] == player and board[space + 2] == player:
                print(f"{player} wins, Diagonal")
                change_board()
                game = False
                break

        if board[4] == player:
            if board[0] == player and board[8] == player:
                change_board()
                print(f"{player} wins, Diagonal")
                game = False
                break
            elif board[2] == player and board[6] == player:
                change_board()
                print(f"{player} wins, Diagonal")
                game = False
                break

    round += 1
