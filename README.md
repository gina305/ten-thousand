# Ten-thousand Dice Game

## Feature Tasks and Requirements
* Create a project named ten-thousand.
* Today is all about tackling the highest risk and/or highest priority features - scoring and dice rolling. 
  * Define a GameLogic class in ten_thousand/game_logic.py file.
  * Handle calculating score for dice roll
    * Add calculate_score static method to GameLogic class.
    * The input to calculate_score is a tuple of integers that represent a dice roll.
    * The output from calculate_score is an integer representing the roll’s score according to rules of game.
* Handle rolling dice
  * Add roll_dice static method to GameLogic class.
  * The input to roll_dice is an integer between 1 and 6.
  * The output of roll_dice is a tuple with random values between 1 and 6.
  * The length of tuple must match the argument given to roll_dice method.
