def valid(x, y, rows, cols, matrix, visited):
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and not visited[x][y]


def shortest_path(matrix, start_pnt, end_pnt):
    rows, cols = len(matrix), len(matrix[0])
    visited = []
    distance = 0
    queue = [(start_pnt[0], start_pnt[1], distance)]

    for i in range(rows):
        rows = []
        for j in range(cols):
            rows.append(False)
        visited.append(rows)    

    while queue:
        x, y, distance = queue.pop(0)
        if (x, y) == end_pnt:
            return distance
        else:
            for direction_x, direction_y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_x, new_y = x + direction_x, y + direction_y
                if valid(new_x, new_y, len(rows), cols, matrix, visited):
                    queue.append((new_x, new_y, distance + 1))
                    visited[new_x][new_y] = True

    return -1

def main():
    with open('input.txt', 'r') as file:
        start = tuple(map(int, file.readline().strip().split(', ')))
        end = tuple(map(int, file.readline().strip().split(', ')))
        rows, cols = map(int, file.readline().strip().split(', '))
        matrix = [list(map(int, file.readline().strip()[1:-1].split())) for _ in range(rows)]

    result = shortest_path(matrix, start, end)

    with open('output.txt', 'w') as file:
        file.write(str(result))

if __name__ == "__main__":
    main()
