class Jedi:
  is_a_good_person = True
  __private_attr = "OK"

  def __init__(self, name, saber, *args, **kwargs):
    self.name = name
    self.saber = saber

  def fight(self, *args, **kwargs):
    print("pew pew pew")

  @staticmethod
  def static_method():
    print("An static method")

class JediMaster(Jedi):
  def __init__(self, name, saber, midichlorians=5000, *args, **kwargs):
    self.midichlorians = midichlorians
    super().__init__(name, saber, *args, **kwargs)

  def give_advic(self):
    print("Fear is the path to the dark side.")

YODA = JediMaster(name="Yoda", saber="Green", midichlorians=7700)

# print(JediMaster.is_a_good_person)
# qui_gon = JediMaster(name="Qui Gon Jinn", saber="Green",
#   midichlorians=10000)
# print(qui_gon.name)
# print(qui_gon.saber)
# print(qui_gon.midichlorians)
# qui_gon.fight()
# qui_gon.give_advic()
# print(JediMaster.static_method())
