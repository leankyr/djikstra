



def main():
    matrix = [[0, 6, 10, 1, 10], [6, 0, 5, 2, 2], [10, 5, 0, 10, 5], [1, 2, 10, 0, 2], [10, 2, 5, 2, 0]]
    k = 0 # source vertex
    m = 5 # num of elements in row
    n = 5 # num of elements in col
    cost = [[0 for x in range(m)] for x in range(1)]
    print (cost)
    offsets = []
    offsets.append(k)
    elepos=0
    print(offsets)
    for j in range(m):
        cost[0][j] = matrix[k][j]
    mini = 999
    for x in range(m - 1):
        mini = 999
        for j in range(m):
            if cost[0][j] <= mini and j not in offsets:
                mini = cost[0][j]
                elepos = j
        offsets.append(elepos)
        for j in range(m):
            if cost[0][j] > cost[0][elepos] + matrix[elepos][j]:
                cost[0][j] = cost[0][elepos] + matrix[elepos][j]
    print("The shortest path", offsets)
    print("The cost to various vertices in order", cost)


if __name__ == '__main__':
    # execute only if run as a script
    main()

