import random
import re

class Game:
  play_tokens = ["O", "X"]

  def get_positions_grid(self):
    grid = ""
    start_row = 1
    end_row = 9

    for i in range(start_row, end_row + 1):
      if (i + 1) % 3 == 0:
        pos_range = range(i - 1, i + 2)
        tmpl = " {} "
        positions = [tmpl.format(str(j)) for j in pos_range]
        grid += "|".join(positions) + "\n"
      elif i % 3 == 0 and i != end_row:
        grid += "___|___|___" + "\n"
      else:
        grid += "   |   |   " + "\n"

    return grid

  def get_board_grid(self, board_list):
    board = ""
    def_row = "   |   |   "

    for i in range(len(board_list)):
      board += def_row + "\n"

      entries = []
      for entry in board_list[i]:
        fixed_entry = " " if entry == "" else entry
        formatted_entry = " {} ".format(fixed_entry)
        entries.append(formatted_entry)

      board += "|".join(entries) + "\n"

      if i < len(board_list) - 1:
        board += "___|___|___" + "\n"
      else:
        board += def_row + "\n"

    return board

  def get_player_token(self, prompt):
    while True:
      input_token = input(prompt + " ").strip()
      uc_token = input_token.upper()

      if uc_token == "":
        print("Please enter a valid value")
      elif uc_token not in self.play_tokens:
        print('"{}" is not a valid value'.format(input_token))
      else:
        return uc_token

  def get_cpu_token(self, player_token):
    for token in self.play_tokens:
      if token != player_token:
        return token

  def get_player_position(self, prompt, open_positions):
    while True:
      player_position_str = input(prompt + " ").strip()
      match = re.match(r"^\d$", player_position_str)

      if player_position_str == "":
        print("Please enter a valid value")
      elif match is None:
        print('"{}" is an invalid position'.format(player_position_str))
      else:
        player_position_int = int(player_position_str)

        if player_position_int not in open_positions:
          print('"{}" is not an open position'.format(player_position_str))
        else:
          return player_position_int

  def get_cpu_position(self, open_positions):
    return random.choice(open_positions)
