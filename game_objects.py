import random

RANKS = {"A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1}
SUIT =["H", "D", "C", "S"]

class Player:
  def __init__(self, player_input=None, weapon=None, previous_turn=None):
    self.health = 20
    self.weapon = weapon
    self.previous_turn = previous_turn
    self.player_input = player_input

  def clean_input(self):
    self.player_input = self.player_input.strip().lower()
    return self.player_input

  def player_choice(self):
    player_input = input("Player Choice: ")
    self.previous_turn = player_input

  def equip_weapon(self):
    pass

class Dungeon:
  def __init__(self, player):
    self.player = player
    self.room = []
    self.deck = Deck()
    self.deck.create_deck()
    self.room_count = self.deck.size // 4

  def create_room(self):
    self.room = self.deck[:4]
    self.deck = self.deck[5:]

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
  def __init__(self, rank, suit):
    super().__init__(rank, suit)
    self.damage = rank
    self.enemies_slain = []