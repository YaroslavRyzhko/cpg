from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        if color not in ['white', 'black']:
            raise ValueError("Color must be 'white' or 'black'")
        if not self.is_position_on_board(position):
            raise ValueError("Position must be within the board limits (1-8 for both row and column)")
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        if self.color == 'white':
            if row == 2:
                moves.append((row + 2, col))
            moves.append((row + 1, col))
        else:  # black pawn
            if row == 7:
                moves.append((row - 2, col))
            moves.append((row - 1, col))
        
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        # Diagonální pohyby
        for i in range(1, 8):
            moves.append((row + i, col + i))  # dolů doprava
            moves.append((row + i, col - i))  # dolů doleva
            moves.append((row - i, col + i))  # nahoru doprava
            moves.append((row - i, col - i))  # nahoru doleva
        
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    
    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        # Horizontální a vertikální pohyby
        for i in range(1, 9):
            if i != row:
                moves.append((i, col))  # vertikální pohyby
            if i != col:
                moves.append((row, i))  # horizontální pohyby
        
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    
    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        # Kombinace pohybů věže a střelce
        for i in range(1, 9):
            if i != row:
                moves.append((i, col))  # vertikální pohyby
            if i != col:
                moves.append((row, i))  # horizontální pohyby

        for i in range(1, 8):
            moves.append((row + i, col + i))  # dolů doprava
            moves.append((row + i, col - i))  # dolů doleva
            moves.append((row - i, col + i))  # nahoru doprava
            moves.append((row - i, col - i))  # nahoru doleva
        
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    
    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())

    knight = Knight("white", (8, 4))
    print(knight)
    print(knight.possible_moves())

    pawn1 = Pawn("white", (2, 3))
    print(pawn1)
    print(pawn1.possible_moves())

    pawn2 = Pawn("black", (6, 3))
    print(pawn2)
    print(pawn2.possible_moves())

    bishop1 = Bishop("black", (5, 4))
    print(bishop1)
    print(bishop1.possible_moves())

    bishop2 = Bishop("white", (5, 8))
    print(bishop2)
    print(bishop2.possible_moves())

    rook1 = Rook("white", (4, 4))
    print(rook1)
    print(rook1.possible_moves())

    rook2 = Rook("black", (1, 1))
    print(rook2)
    print(rook2.possible_moves())

    queen1 = Queen("white", (1, 4))
    print(queen1)
    print(queen1.possible_moves())

    queen2 = Queen("black", (8, 5))
    print(queen2)
    print(queen2.possible_moves())

    king1 = King("white", (2, 6))
    print(king1)
    print(king1.possible_moves())

    king2 = King("black", (5, 1))
    print(king2)
    print(king2.possible_moves())