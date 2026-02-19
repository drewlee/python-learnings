from board import Board
from game import Game
from utils import repeat_char

def get_formatted_greeting(greeting):
  dashes = repeat_char("-", len(greeting))

  message = dashes + "\n"
  message += "\n"
  message += greeting + "\n"
  message += "\n"
  message += dashes + "\n"

  return message

def get_positions_prompt(tmpl_str, open_positions):
  open_positions_str = [str(pos) for pos in open_positions]
  return tmpl_str.format(", ".join(open_positions_str))

def run():
  board = Board()
  game = Game()

  greeting = "YO YO! PYTHON TIC TAC TOE!"
  print(get_formatted_greeting(greeting))

  player_token_prompt = "Which token would you like to use, X or O?"
  player_token = game.get_player_token(player_token_prompt)
  print("Picked {}".format(player_token))
  print("")

  cpu_token = game.get_cpu_token(player_token)

  print("Positions correspond to the following diagram:")
  print(game.get_positions_grid())

  while True:
    print('Please enter a position to place an "{}" into'.format(player_token))

    open_positions = board.get_open_positions()
    position_prompt = get_positions_prompt("Available positions are {}:", open_positions)
    player_position = game.get_player_position(position_prompt, open_positions)
    is_win = board.play_turn(player_position, player_token)

    print('Placed "{}" at position {}'.format(player_token, str(player_position)))
    print(game.get_board_grid(board.get_board_list()))

    if len(open_positions) == 1:
      print("The game is a draw")
      break

    if is_win:
      print("Congratulations, you have won the game!")
      break

    open_positions = board.get_open_positions()
    cpu_position = game.get_cpu_position(open_positions)
    is_win = board.play_turn(cpu_position, cpu_token)

    print('The CPU has placed "{}" at position {}'.format(cpu_token, cpu_position))
    print(game.get_board_grid(board.get_board_list()))

    if is_win:
      print("Sorry, you've lost the game.")
      break

run()
