class Board:
  positions_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                    4: (1, 0), 5: (1, 1), 6: (1, 2),
                    7: (2, 0), 8: (2, 1), 9: (2, 2)}

  def __init__(self):
    self.setup_board()

  def setup_board(self):
    self.board = []

    for i in range(3):
      row = []
      for j in range(3):
        row.append("")
      self.board.append(row)
  
  def get_board_list(self):
    return self.board

  def play_turn(self, position, token):
    x, y = self.positions_dict[position]

    if self.board[x][y] == "":
      self.board[x][y] = token
    else:
      print("Position is already taken")
      return False

    return self.is_win(token)

  def is_win(self, token):
    win_row_positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                         [1, 4, 7], [2, 5, 8], [3, 6, 9],
                         [1, 5, 9], [3, 5, 7]]

    for row in win_row_positions:
      is_win = True
      for pos in row:
        x, y = self.positions_dict[pos]
        if self.board[x][y] != token:
          is_win = False
      if is_win:
        return True

    return False

  def get_open_positions(self):
    positions = []

    for pos, value in self.positions_dict.items():
      x, y = value
      if self.board[x][y] == "":
        positions.append(pos)

    return positions
