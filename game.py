chess_map = [["R1", "N1", "B1", "Q1", "K1", "B1", "N1", "R1"],
       ["P1", "P1", "P1", "P1", "P1", "P1", "P1", "P1"],
       ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
       ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
       ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
       ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
       ["P2", "P2", "P2", "P2", "P2", "P2", "P2", "P2"],
       ["R2", "N2", "B2", "Q2", "K2", "B2", "N2", "R2"]]

def get_can_move_king(board, x, y, index):
    # キングの動ける場所を計算
    moves = []
    king_moves = [(1, 0), (0, 1), (-1, 0), (0, -1),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for dx, dy in king_moves:
        c, r = x + dx, y + dy
        if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == "  " or board[r][c][-1] != str(index)):
            a = board[r][c][-1]
            moves.append((c, r))
    return moves
def get_can_move_rook(board, x, y, index):
    # ルークの動ける場所を計算
    moves = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 上下左右の方向
    for dx, dy in directions:
        c, r = x + dx, y + dy
        while True:
            if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == "  " or board[r][c][-1] != str(index)):
                moves.append((c, r))
                if board[r][c][-1] != str(index):
                    break
            else:
                break
            c+= dx
            r += dy
    return moves
def get_can_move_bishop(board, x, y, index):
    # ビショップの動ける場所を計算
    moves = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # 上下左右の方向
    for dx, dy in directions:
        c, r = x + dx, y + dy
        while True:
            if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == "  " or board[r][c][-1] != str(index)):
                moves.append((c, r))
                if board[r][c][-1] != str(index):
                    break
            else:
                break
            c += dx
            r += dy
    return moves
def get_can_move_night(board, x, y, index):
    # ナイトの動ける場所を計算
    moves = []
    night_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    for dx, dy in night_moves:
        c, r = x + dx, y + dy
        if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == "  " or board[r][c][-1] != str(index)):
            moves.append((c, r))
    return moves
def get_can_move_pown(board, x, y, index):
    # ポーンの動ける場所を計算
    moves = []
    pown_moves = []
    if (index == 1 and y == 1):
        pown_moves = [(0, 1), (0, 2)]
    elif (index == 2 and y == 6):
        pown_moves = [(0, -1), (0, -2)]
    elif index == 1:
        pown_moves = [(0, 1)]
    elif index == 2:
        pown_moves = [(0, -1)]
    for dx, dy in pown_moves:
        c, r = x + dx, y + dy
        if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == "  " or board[r][c][-1] != str(index)):
            a = board[r][c][-1]
            moves.append((c, r))
    return moves
def get_can_move_queen(board, x, y, index):
    # queen
    moves = []
    direction = []
    direction += get_can_move_rook(board, x, y, index)
    direction += get_can_move_bishop(board, x, y, index)
    for dx, dy in direction:
        c, r = x + dx, y + dy
        while True:
            if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == "  " or board[r][c][-1] != str(index)):
                moves.append((c, r))
                if board[r][c][-1] != str(index):
                    break
            else:
                break
            c += dx
            r += dy
    return moves

print("ゲームを開始します")
print("現在の盤面")
for i in range(8):
    for j in range(8):
        print(chess_map[i][j] + " ", end="")
    print()
print()
select_piece = ""
select_can_moves = []
player_id = 1
player_x = 0
player_y = 0
while True:
    while True:
        player_x = int(input("piece x ->"))
        player_y = int(input("piece y ->"))

        if chess_map[player_y][player_x] == "  " or chess_map[player_y][player_x][-1] != str(player_id):
            print("そこは動かせません")
        else:
            select_piece = chess_map[player_y][player_x]
            break

    print("動かせる場所一覧")
    if select_piece[0] == "K":
        select_can_moves = get_can_move_king(chess_map, player_x, player_y, player_id)
    if select_piece[0] == "R":
        select_can_moves = get_can_move_rook(chess_map, player_x, player_y, player_id)
    if select_piece[0] == "Q":
        select_can_moves = get_can_move_queen(chess_map, player_x, player_y, player_id)
    if select_piece[0] == "N":
        select_can_moves = get_can_move_night(chess_map, player_x, player_y, player_id)
    if select_piece[0] == "B":
        select_can_moves = get_can_move_bishop(chess_map, player_x, player_y, player_id)
    if select_piece[0] == "P":
        select_can_moves = get_can_move_pown(chess_map, player_x, player_y, player_id)
    print(select_can_moves)
    go_x = -1
    go_y = -1
    while True:
        tox = int(input("to x ->"))
        toy = int(input("to y ->"))

        for select_x, select_y in select_can_moves:
            if select_x == tox and select_y == toy:
                go_x = tox
                go_y = toy
        if go_x == -1 or go_y == -1:
            print("そこには移動できません")
        else:
            break
    if chess_map[go_y][go_x] != "  ":
        print("あなたは" + chess_map[go_y][go_x] + "を倒した")
        if chess_map[go_y][go_x][0] == "K": 
            print("あなたの勝ちです")
            break
    chess_map[go_y][go_x] = select_piece
    chess_map[player_y][player_x] = "  "
    player_x = go_x
    player_y = go_y
    for i in range(8):
        for j in range(8):
            print(chess_map[i][j] + " ", end="")
        print()
    print()
