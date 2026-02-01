import random
import re

RANKS = {"A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1}
SUIT =["H", "D", "C", "S"]

class Player:
  def __init__(self, player_input=None, weapon=None, previous_turn=None):
    self.health = 20
    self.weapon = weapon
    self.previous_turn = previous_turn
    self.player_input = player_input

  def clean_input(self):
    cleaned = []
    cleaned.append(re.findall(r"\d+", self.player_input))
    cleaned.append(re.findall(r"\w", self.player_input))
    return cleaned

  def player_choice(self):
    self.player_input = input("Player Choice: ")
    cleaned = self.clean_input()
    self.previous_turn = cleaned
    
    if ("C" or "S") in cleaned:
      if self.weapon:
        if self.weapon.enemies_slain[-1].rank > RANKS[cleaned[0]]:
          second_choice = input("Fight barehanded? ")
          second_choice = second_choice.strip().lower()
          if second_choice == ("y" or "yes"):
            self.health -= RANKS[cleaned[0]]
          else:
            reduced = RANKS[cleaned[0]] - self.weapon.damage
            if reduced < 0:
              pass
            self.health -= reduced

      self.health -= RANKS[cleaned[0]]

    if "H" in cleaned:
      self.health += RANKS[cleaned[0]]
      if self.health > 20:
        self.health = 20

    if "D" in cleaned:
      self.equip_weapon()

  def equip_weapon(self):
      weapon_rank = RANKS[self.player_input[0]]
      self.weapon = Weapon(weapon_rank)

class Dungeon:
  def __init__(self, player):
    self.player = player
    self.room = []
    self.deck = Deck()
    self.deck.create_deck()
    self.room_count = self.deck.size // 4

  def create_starting_room(self):
    self.room = self.deck.cards[:4]
    self.deck.cards = self.deck.cards[5:]

  def create_room(self):
    self.room.append(self.deck.cards[:3])
    self.deck.cards = self.deck.cards[4:]

  def pass_turn(self):
    if self.room_count == 0:
      raise Exception("No rooms left")
    if self.player.previous_turn == "p":
      raise Exception("Passed previous turn")
    
    self.deck.append(random.shuffle(self.room))
    self.room = self.deck[:4]

class Card:
  def __init__(self, rank, suit):
    self.suit = suit
    self.rank = rank

  def __repr__(self):
    return f"{self.rank}{self.suit}"

class Deck:
  def __init__(self):
    self.cards = []
    self.size = len(self.cards)
  
  def create_deck(self):
    for suit in SUIT:
      for rank in RANKS:
        if (suit == "H" or suit == "D") and RANKS[rank] > 10:
          continue
        self.cards.append(Card(rank, suit))
    random.shuffle(self.cards)

class Weapon(Card):
  def __init__(self, rank):
    super().__init__(rank, None)
    self.damage = rank
    self.enemies_slain = []