



def main():
    adj_mat = [[0, 6, 0, 1, 0], [6, 0, 5, 2, 2], [0, 5, 0, 0, 5], [1, 2, 0, 0, 2], [0, 2, 5, 2, 0]]
    for i in range(0,len(adj_mat)):
        for j in range(0, len(adj_mat[0])):
            print (adj_mat[i][j], end=" ")

        print(" ")

        V = []
        U = [0, 1, 2, 3, 4]
        SD = [0, 100, 100, 100, 100]
        PV = [0 ,0, 0 ,0 ,0]
    for i in range(0, len(adj_mat[0])):
        



if __name__ == "__main__":
    # execute only if run as a script
    main()

