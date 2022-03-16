def solution(board, moves):
    doll = 0
    bucket = []

    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] != 0:
                bucket.append(board[i][j-1])
                board[i][j-1] = 0
                break
    
        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            bucket.pop(-1)
            bucket.pop(-1)
            doll += 2

    return doll