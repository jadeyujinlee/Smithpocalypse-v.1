
import turtle
import time
from minigame import *
from ckpointgraphics import graphics

#opens and reads Gametext file
r = open( "Gametext.txt", "r")
text = r.readlines()
r.close()
from data import *



class tellstory:
  def __init__(self):
    self.greg = turtle.Turtle()
    self.play = "Y"
    self.end = "go"
    self.num = []
    self.supply = ''
  def set_play(self):
    #propmts user if they wish to continue after every death
    self.play = input("Would you like to continue playing? Y or N:")
    if self.play not in opt:
      print("Invalid input try again")
      self.set_play()
  def start(self):
    #reads text from dictionary
    try:
      list = gameDict[str(self.num)]
      for i in list:
        print(i)
    except KeyError:
      print("something went wrong. Start Over")
      self.num = []
      self.start()
  def decide(self):
    #Checks if dictionary key is a death option and resets key to last checkpoint
    if self.num in die_1:
      self.set_play()
      self.num = []
    elif self.num in die_2:
      self.set_play()
      self.num = ['b', 'a', 'a', 'b', 'b']
    elif self.num in die_3:
      self.set_play()
      self.num = ['b', 'a', 'a', 'b', 'b', 'b', 'b', 'a', 'b']
    else:
      #prompts the user to make next choice and appends the dictonary key accordingly
      dec = input(">>>")
      if dec.upper() == "A":
        self.num.append("a")
      elif dec.upper() == "B":
        self.num.append("b")
      else:
        print("Invalid input try again")
        self.decide()
  def choice_office(self):
    #special option where user must input wifi password to continue
    self.num = "password"
    self.start()
    password = input("Password:")
    while password.lower() != "sophiasmith":
      print("Try again")
      password = input("Password:")
    self.num = ['b', 'a', 'a', 'b', 'b', 'b', 'a', 'a', 'b']
    
  def equipment(self):
    #special option where user must chose specific supply to use
    self.num = "do"
    self.start()
    self.supply = input(">>>")
    if self.supply == "softball bat":
      self.num = "bat"
      self.start()
      time.sleep(1)
      self.set_play()
      self.num = ['b', 'a', 'a', 'b', 'b', 'b', 'b', 'a', 'b']
    elif self.supply == "water bottle":
      self.num = ['b', 'a', 'a', 'b', 'b', 'b', 'b', 'a', 'b', 'b', 'b', 'b']
    elif self.supply == "first aid kit":
      self.num = "aid"
      self.start()
      time.sleep(1)
      self.set_play()
      self.num = ['b', 'a', 'a', 'b', 'b', 'b', 'b', 'a', 'b']
    else:
      print("Invalid input try again")
      self.equipment()


def main():
  p = tellstory()
  x = graphics() #introduces class from ckpointgrpahics file
  if p.play != "N": #only runs while user opts to continue playing
    while p.end == "go": #loops until final dictionary key
      if p.num == end:
        p.end = "stop"
      if p.num == office_code:
        p.choice_office()
        time.sleep(1)
        p.start()
        p.decide()
      if p.num == check_1:
        x.drawparkhouse(x.greg)
      if p.num == check_2:
        x.drawcampuscenter(x.greg)
      if p.num == supply_code:
        p.equipment()
        time.sleep(1)
        p.start()
        p.decide()
      else:
        if p.play != "N":
          p.start()
          if p.num != end:
            p.decide()
          time.sleep(1)
      
if __name__ == "__main__":
  main()
  time.sleep(1)
  minigame()
  


