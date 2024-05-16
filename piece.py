class Piece:
    def __init__(self, name, x, y, move_vector):
        self.name = name
        self.x = 0
        self.y = 0
        self.move_vector = [move_vector.copy()] # x, y, len x, yは法線ベクトル
                    