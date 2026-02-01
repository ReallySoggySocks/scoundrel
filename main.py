from game_objects import Player, Dungeon, Deck # type: ignore

def main():
  player = Player()
  dungeon = Dungeon(player)
  print(dungeon.deck.cards)

if __name__ == "__main__":
  main()