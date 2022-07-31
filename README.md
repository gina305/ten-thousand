# Ten-thousand Dice Game

## Feature Tasks and Requirements

### Feature 1:
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

### Feature 2:
#### Feature Tasks
Write the following method for the Linked List class:

* kth from end
* argument: a number, k, as a parameter.
* Return the node’s value that is k places from the tail of the linked list.
* You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

#### Unit Tests
Write tests for the following scenarios, and any other cases that help you ensure your code is working as expected.

1. Where k is greater than the length of the linked list
2. Where k and the length of the list are the same
3. Where k is not a positive integer
4. Where the linked list is of a size 1
5. “Happy Path” where k is not at the end, but somewhere in the middle of the linked list