import random


# # For each die, check the rules list.
# # f
#  for rule in rules:
#    print(rule)
# # if die in tuple then do the following:
#   if die
# # output from calculate_score is an integer representing the roll’s score according to rules of game.

rules = [
        (tuple(), 0),
        ((1,), 100),
        ((1, 1), 200),
        ((1, 1, 1), 1000),
        ((1, 1, 1, 1), 2000),
        ((1, 1, 1, 1, 1), 3000),
        ((1, 1, 1, 1, 1, 1), 4000),
        ((2,), 0),
        ((2, 2), 0),
        ((2, 2, 2), 200),
        ((2, 2, 2, 2), 400),
        ((2, 2, 2, 2, 2), 600),
        ((2, 2, 2, 2, 2, 2), 800),
        ((3,), 0),
        ((3, 3), 0),
        ((3, 3, 3), 300),
        ((3, 3, 3, 3), 600),
        ((3, 3, 3, 3, 3), 900),
        ((3, 3, 3, 3, 3, 3), 1200),
        ((4,), 0),
        ((4, 4), 0),
        ((4, 4, 4), 400),
        ((4, 4, 4, 4), 800),
        ((4, 4, 4, 4, 4), 1200),
        ((4, 4, 4, 4, 4, 4), 1600),
        ((5,), 50),
        ((5, 5), 100),
        ((5, 5, 5), 500),
        ((5, 5, 5, 5), 1000),
        ((5, 5, 5, 5, 5), 1500),
        ((5, 5, 5, 5, 5, 5), 2000),
        ((6,), 0),
        ((6, 6), 0),
        ((6, 6, 6), 600),
        ((6, 6, 6, 6), 1200),
        ((6, 6, 6, 6, 6), 1800),
        ((6, 6, 6, 6, 6, 6), 2400),
        ((1, 2, 3, 4, 5, 6), 1500),
        ((2, 2, 3, 3, 4, 6), 0),
        ((2, 2, 3, 3, 6, 6), 1500),
        ((1, 1, 1, 2, 2, 2), 1200),
    ]
def random_dice():
  return random.randint(1, 6)
recorded = []

new_tuple = []
last_rolled = []


#Define a GameLogic class in ten_thousand/game_logic.py file.
class GameLogic:

  @staticmethod
  def calculate_score(input=(2, 2, 3, 3, 6, 6)):
      scored_points = []
      if input == ():
          return 0

      input = sorted(list(input))
      # print(straight_dice)
      for rule in rules:

          # Define variable for iteration
          score = rule[1]
          rule = list(rule[0])

          #Conditionally add score
          if input == rule:
              scored_points.append(score)
              #print(input, rule, score)
      return sum(scored_points)

  @staticmethod
  def roll_dice(num_dice):
    # Loop through the number of dice and generate a random number

    x = 0
    list_values = []

    while x < num_dice:
      x = x + 1
      die_roll = random_dice()

        # Append to the list

      list_values.append(die_roll)

    return tuple(list_values)


"""* A class method takes cls as the first parameter while a static method needs no specific parameters.
* A class method can access or modify the class state while a static method can’t access or modify it.
* In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
* We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
"""

