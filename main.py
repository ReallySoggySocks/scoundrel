import sys

from game_objects import Player, Dungeon, Deck # type: ignore

def main():
  player = Player()
  dungeon = Dungeon(player)
  dungeon.create_starting_room()

  while True:
    if player.player_input == ("q" or "quit"):
      sys.exit()

    if len(dungeon.room) == 3:
      dungeon.create_room()

    for card in dungeon.room:
      print(card, end=" | ")
    print("\n")

    player.player_choice(dungeon)

    break
  return

if __name__ == "__main__":
  main()