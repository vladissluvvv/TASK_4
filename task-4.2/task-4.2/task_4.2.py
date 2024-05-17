def spiral(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, di = 0, 0, 0

    for i in range(1, n * n + 1):
        matrix[x][y] = i
        nx, ny = x + dx[di], y + dy[di]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0:
            x, y = nx, ny
        else:
            di = (di + 1) % 4
            x, y = x + dx[di], y + dy[di]

    for row in matrix:
        print(" ".join(f"{elem:2}" for elem in row))

n = int(input("¬ведите число "))
spiral(n)



