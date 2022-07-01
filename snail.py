DIRECTIONS = [[0, 1], [0, -1], [-1, 0], [1, 0]] # 상하좌우

def snail(size: int, x: int, y: int, board: list[list[int]]):
    queue = [(x, y, 0, 0)]
    arrived = []

    while queue:
        x, y, move, distance = queue.pop(0)
        if (x < 0 or x > size + 1) or (y < 0 or y > size + 1): # 가장자리를 벗어난 경우
            continue

        if move > 7: # 7번 안에 찾지 못한 경우
            continue

        if (x == 0 or x == size + 1) or (y == 0 or y == size + 1): # 도달한 경우
            arrived.append(distance)
            continue

        delta_move = board[y - 1][x - 1]
        for delta_x, delta_y in DIRECTIONS:
            queue.append((x + delta_move * delta_x,
                            y + delta_move * delta_y,
                            move + 1,
                            distance + delta_move))

    return min(arrived) if arrived else 0

if __name__ == "__main__":
    iteration = int(input())

    for _ in range(iteration):
        size, x, y = map(int, input().split())
        board = []
        
        for __ in range(size):
            board.append(list(map(int, input().split())))

        result = snail(size, x, y, board)
        print(result)
