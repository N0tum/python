class Textile:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_tissue_c(self):
        return self.size / 6.5 + 0.5

    def get_tissue_j(self):
        return self.height * 2 + 0.3

    @property
    def get_tissue_full(self):
        return str(f'Total tissue {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textile):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.tissue_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Tissue for coat: {self.tissue_c}'


class Jacket(Textile):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.tissue_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Tissue for jacket: {self.tissue_j}'


coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_tissue_full)
print(jacket.get_tissue_full)
print(jacket.get_tissue_c())
print(jacket.get_tissue_j())
