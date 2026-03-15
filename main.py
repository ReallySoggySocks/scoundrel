import sys
import os

from game_objects import Player, Dungeon, Deck # type: ignore

def main():
  player = Player()
  dungeon = Dungeon(player)
  dungeon.create_starting_room()

  while True:
    if player.health <= 0:
      print("Game Over!")
      break

    if len(dungeon.room) == 1:
      dungeon.create_room()

    print("-------------------")
    for card in dungeon.room:
      print(card, end=" | ")
    print("\n")

    print(f"Player Health: {player.health}")
    print(f"Weapon: {player.weapon}")
    if player.weapon and len(player.weapon.enemies_slain) > 0:
      print("Last Enemy Slain: ", player.weapon.enemies_slain[-1])
    print("-------------------")

    player.player_choice(dungeon)

    #os.system("clear")

  return

if __name__ == "__main__":
  main()