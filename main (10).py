class Player():
      
    def play(self):
        print("The player is playing cricket")
          
class Batsman(Player):
      
    def play(self):
        print("The batsman is batting")
          
class Bowler(Player):
      
    def play(self):
        print("The bowler is bowling")
          
obj1 = Batsman()
obj2 = Bowler()
  
obj1.play()
obj2.play()