def checkmate(board):
    rows = board.strip().split('\n')
    size = len(rows)
    king_pos = None


    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                king_pos = (r, c)
                break
    
    if not king_pos:
        return

    kr, kc = king_pos

   
    def is_attacked(dr, dc, pieces):
        nr, nc = kr + dr, kc + dc
        while 0 <= nr < size and 0 <= nc < size:
            char = rows[nr][nc]
            if char != '.':
                return char in pieces 
            nr += dr
            nc += dc
        return False

    
    straight = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in straight:
        if is_attacked(dr, dc, ['R', 'Q']):
            print("Success")
            return

    
    diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in diagonal:
        if is_attacked(dr, dc, ['B', 'Q']):
            print("Success")
            return

    
    pawn_moves = [(-1, -1), (-1, 1)]
    for dr, dc in pawn_moves:
        nr, nc = kr + dr, kc + dc
        if 0 <= nr < size and 0 <= nc < size:
            if rows[nr][nc] == 'P':
                print("Success")
                return

    
    print("Fail")