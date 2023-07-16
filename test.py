def cyclotron(particle, size):
    matrix = [[1] * size for _ in range(size)]

    if particle == "e":
        for i in range(size):
            matrix[0][i] = "e"
            if i != size - 1:
                matrix[i + 1][-1] = "e"
    elif particle == "p":
        for i in range(size):
            matrix[0][i] = matrix[i][0] = matrix[-1][i] = matrix[i][
                -1
            ] = matrix[-2][-2] = "p"
            matrix[-1][-1] = 1
    elif particle == "n":
        matrix[0] = ["n"] * size

    return matrix
