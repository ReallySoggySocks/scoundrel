import random
import re

RANKS = {"A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1}
SUIT =["H", "D", "C", "S"]

class Player:
  def __init__(self, player_input, weapon=None, previous_turn=None):
    self.health = 20
    self.weapon = weapon
    self.previous_turn = previous_turn
    self.player_input = player_input

  def clean_input(self):
    self.input = self.input.strip().lower()
    return self.input

  def player_choice(self):
    pass

  def equip_weapon(self):
    pass

class Dungeon:
  def __init__(self, player):
    self.player = player
    self.room = []
    self.deck = Deck.create_deck()
    self.room_count = self.deck.size // 4

  def create_room(self):
    self.room = self.deck[:4]
    self.deck = self.deck[5:]

  def pass_turn(self):
    if self.room_count is 0:
      raise Exception("No rooms left")
    if self.player.previous_turn is "p":
      raise Exception("Passed previous turn")
    
    self.deck.append(random.shuffle(self.room))
    self.room = self.deck[:4]

class Card:
  def __init__(self, rank, suit):
    self.suit = suit
    self.rank = rank

class Deck:
  def __init__(self):
    self.cards = []
    self.size = len(self.cards)
  
  def create_deck(self):
    for suit in SUIT:
      for rank in RANKS:
        if suit is "D" or suit is "H" and rank[rank] > 10:
          continue
        self.cards.append(Card(rank, suit))
    self.cards = random.shuffle(self.cards)

class Weapon(Card):
  def __init__(self, rank, suit):
    super().__init__(rank, suit)
    self.damage = rank
    self.enemies_slain = []