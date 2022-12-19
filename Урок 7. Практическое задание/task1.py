class Matrix:
    def __init__(self, franchises):
        self.franchises = franchises

    def __str__(self):
        return '\n'.join(map(str, self.franchises))

    def __add__(self, sequel):
        c = []
        for i in range(len(self.franchises)):
            c.append([])
            for j in range(len(self.franchises[0])):
                c[i].append(self.franchises[i][j] + sequel.franchises[i][j])
        return '\n'.join(map(str, c))


reload = [[1, 3, 4], [1, -2, 2], [1, 4, -4]]
revolution = [[5, -6, 9], [2, 5, 7], [1, 3, 2]]

thematrix2 = Matrix(reload)
thematrix3 = Matrix(revolution)

print(thematrix2 + thematrix3)
