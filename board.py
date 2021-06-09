import numpy as np

class Board:
    """ Chess Board Representation for Program"""
    def __init__(self):

        # white pieces bit boards
        self.w_K_board = np.uint64()
        self.w_Q_board = np.uint64()
        self.w_R_board = np.uint64()
        self.w_N_board = np.uint64()
        self.w_B_board = np.uint64()
        self.w_P_board = np.uint64()

        # black pieces bit boards
        self.b_K_board = np.uint64()
        self.b_Q_board = np.uint64()
        self.b_R_board = np.uint64()
        self.b_N_board = np.uint64()
        self.b_B_board = np.uint64()
        self.b_P_board = np.uint64()

    def set_pieces(self):
        """ Setup board as regular chess setup"""
        self.set_white()
        self.set_black()

    def set_white(self):
        """ Sets white pieces on board"""
        self.w_K_board = self.set_bit(self.w_K_board, 4)
        self.w_Q_board = self.set_bit(self.w_Q_board, 3)
        self.w_R_board = self.set_bit(self.w_R_board, 0)
        self.w_R_board = self.set_bit(self.w_R_board, 7)
        self.w_N_board = self.set_bit(self.w_N_board, 1)
        self.w_N_board = self.set_bit(self.w_N_board, 6)
        self.w_B_board = self.set_bit(self.w_B_board, 2)
        self.w_B_board = self.set_bit(self.w_B_board, 5)
        for i in range(8, 16):
            self.w_P_board = self.set_bit(self.w_P_board, i)

    def set_black(self):
        """ Sets black pieces on board"""
        self.b_K_board = self.set_bit(self.b_K_board, 4)
        self.b_Q_board = self.set_bit(self.b_Q_board, 3)
        self.b_R_board = self.set_bit(self.b_R_board, 0)
        self.b_R_board = self.set_bit(self.b_R_board, 7)
        self.b_N_board = self.set_bit(self.b_N_board, 1)
        self.b_N_board = self.set_bit(self.b_N_board, 6)
        self.b_B_board = self.set_bit(self.b_B_board, 2)
        self.b_B_board = self.set_bit(self.b_B_board, 5)
        for i in range(8, 16):
            self.b_P_board = self.set_bit(self.b_P_board, i)

    def set_bit(self, board, bit):
        """
        Sets a bit at a certain position to 1
        :param board: bit board being changed
        :param bit: index of bit being changed
        :return:
        """
        return np.uint64(board | np.uint64(1) << np.uint64(bit))

    def clear_bit(self, board, bit):
        """
        Sets a bit at a certain position to 0
        :param board: bit board being changed
        :param bit: index of bit being changed
        :return:
        """
        return board & ~(np.uint64(1) << np.uint64(bit))


    def print_board(self, side="white"):
        str_board = np.array(['.'] * 64)
        board_list = [i for i, bit in enumerate(reversed(str(self.w_K_board)), 1) if bit == '1']
        print(board_list)
        #print(np.reshape(str_board, (8, 8)))




if __name__ == "__main__":
    board = Board()
    board.set_white()
    board.print_board()