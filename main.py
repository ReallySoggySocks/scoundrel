from game_objects import Player, Dungeon, Deck # type: ignore

def main():
  player = Player()
  dungeon = Dungeon(player)
  while True:
    player.player_choice()
    print(player.player_input)
    break
  return

if __name__ == "__main__":
  main()