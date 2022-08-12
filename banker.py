class Banker():

  def __init__(self):
    self.balance = 0
    self.shelved = 0
    pass


  def shelf(self, points):
    self.shelved +=points
    return self.shelved
      
  
  def bank(self):
    self.balance += self.shelved
    self.shelved = 0
    return self.balance
  # bank instance method - adds any points on the shelf to total and resets shelf to 0

# clear shelf method to remove un-banked points
  def clear_shelf(self):
    self.shelved = 0