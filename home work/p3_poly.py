class vehicle():
   def start(self):
      print("starting the vehicle")
class bike(vehicle):
   def start(self):
      print("starting the bike")
class car(vehicle):
   def start(self):
      print("startinf the car")
vobj=vehicle()
vobj.start()
bobj=bike()
bobj.start()
cobj=car()
cobj.start()

