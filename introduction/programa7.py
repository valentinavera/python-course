# bloques de código
a, b = 10, 5
if a > b:
  print("A > B")
print("Fin del if")

if a > b:
  print("A > B")
else:
  print("A <= B")

if a == b:
  print("A == B")
elif a > b:
  print("A > B")
else:
  print("A <= B")

if not a == b:
  print("A != B")  # ! =

if a is b:
  print("A == B") # = =

a = 500 if a > b else 50
print(a)
