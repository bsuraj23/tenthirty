class vehicle():
   def start(self):
      print("starting the vehicle")
class bike(vehicle):
   def start(self):
      print("starting the bike")
      super().start()
obj=bike()
obj.start()      
