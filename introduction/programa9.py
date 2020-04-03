# funciones

# parámetros posicionales
def say_hello(name):
  print("Hi %s" % name)

say_hello("Curso de Python")

def avengers_assemble(av1, av2):
  print("%s, %s" % (av1, av2))

avengers_assemble("Cap", "Ironman")

# parámetros palabra clave
avengers_assemble(av2="Cap", av1="Ironman")

# parámetros arbitratios
def avengers_assemble(*avengers):
  # avengers is a list!
  print(", ".join(avengers))

avengers_assemble("Cap", "Ironman", "Spidy")
avengers_assemble("Cap")

print()
# parámetros arbitrarios palabra clave
def my_gang(girl=None, **guys):
  # guys is a dict
  print("%s as the %s" % (girl, "girl"))
  for role, name in guys.items():
    print("%s as the %s" % (name, role))

my_gang(girl="Cloe", listo="Data", feo="Sloth",
  miedoso="Chunk", apuesto="Mounth", two=2)

# retornar valores
print()
def square(x):
  return x**2

print(square(5))

def rock_n_roll():
  return "Rock", "Roll"

v1, v2 = rock_n_roll()
print("%s & %s" % (v1, v2))

def empty_fn():
  pass

print(empty_fn())

# null -> None

