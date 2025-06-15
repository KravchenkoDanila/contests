from array import array


def read_input():
    import sys
    input_bytes = sys.stdin.read().encode('utf-8')
    buffer = memoryview(input_bytes)

    idx = 0
    while idx < len(buffer) and buffer[idx] == 32:
        idx += 1

    def read_int():
        nonlocal idx
        start = idx
        while idx < len(buffer) and 48 <= buffer[idx] <= 57:
            idx += 1
        return int(buffer[start:idx].tobytes().decode())

    n = read_int()
    m = read_int()
    d = read_int()

    grid = []
    X, x = b'X'[0], b'x'[0]
    O, o = b'O'[0], b'o'[0]

    for _ in range(n):
        row = bytearray(m)
        j = 0
        while j < m:
            c = buffer[idx]
            if c == 10 or c == 32:
                idx += 1
                continue
            row[j] = c
            idx += 1
            j += 1
        grid.append(row)
    return n, m, d, grid


def compute_distance(grid, n, m):
    INF = n + m
    dist = [array('H', [INF] * m) for _ in range(n)]

    X, x = b'X'[0], b'x'[0]

    for i in range(n):
        row = grid[i]
        drow = dist[i]
        for j in range(m):
            if row[j] == x or row[j] == X:
                drow[j] = 0
            else:
                if i > 0:
                    drow[j] = min(drow[j], dist[i - 1][j] + 1)
                if j > 0:
                    drow[j] = min(drow[j], drow[j - 1] + 1)

    for i in reversed(range(n)):
        drow = dist[i]
        for j in reversed(range(m)):
            if i < n - 1:
                drow[j] = min(drow[j], dist[i + 1][j] + 1)
            if j < m - 1:
                drow[j] = min(drow[j], drow[j + 1] + 1)

    return dist


def max_square_size(grid, dist, n, m, d):
    O, o = b'O'[0], b'o'[0]
    best = 0

    prev = array('H', [0] * (m + 1))
    curr = array('H', [0] * (m + 1))

    for i in range(n):
        row = grid[i]
        drow = dist[i]
        for j in range(m):
            if drow[j] >= d and (row[j] == o or row[j] == O):
                curr_val = min(prev[j], prev[j + 1], curr[j]) + 1
                curr[j + 1] = curr_val
                if curr_val > best:
                    best = curr_val
            else:
                curr[j + 1] = 0
        prev, curr = curr, prev

    return best


def main():
    n, m, d, grid = read_input()
    dist = compute_distance(grid, n, m)
    print(max_square_size(grid, dist, n, m, d))


if __name__ == '__main__':
    main()