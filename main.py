print("""
 _   _      _             _             
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ 
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|                                 
""")


def update_board():
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


def set_game_vars():
    global board, game, round, tick, endgame
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    game = True
    round = 1
    tick = "O"
    endgame = False


set_game_vars()

while game:

    if endgame:
        if input("If you want to restart, type 'R' ") == "R":
            set_game_vars()
        else:
            print("Game Closed")
            break

    update_board()
    print(f"round: {round}")

    if tick == "O":
        tick = "X"
    else:
        tick = "O"

    if round < 10:
        to_replace = input(f"{tick}'s move. Place your mark. Numbers 1-9 only. ")
        if not board[int(to_replace) - 1] == "X" and not board[int(to_replace) - 1] == "O":
            board[int(to_replace) - 1] = board[int(to_replace) - 1].replace(board[int(to_replace) - 1], tick)

        else:
            print("invalid move")
            round -= 1
            if tick == "X":
                tick = "O"
            else:
                tick = "X"
    else:
        print("It's a draw")
        endgame = True

    if round >= 3:
        full_row = [tick, tick, tick]
        for index, space in enumerate(board):
            if board[index::3] == full_row:
                update_board()
                print(f"{tick} wins, Vertical")
                endgame = True

            elif index in list(range(0, 7, 3)) and board[index:index + 3] == full_row:
                update_board()
                print(f"{tick} wins, Horizontal")
                endgame = True

        if board[0::4] == full_row or board[2::2][:3] == full_row:
            update_board()
            print(f"{tick} wins, Diagonal")
            endgame = True

    round += 1
