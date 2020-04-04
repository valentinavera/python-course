class ErrorDeDiv(Exception):
  pass

def divide(a, b):
  if b != 0:
    return a/b
  raise ErrorDeDiv

try:
  result = divide(10, 5)
except ErrorDeDiv as e:
  print(e)
else:
  print(result)


# Vista
# controlar el error
# Controlar Error

# Controlador
# try: Error
# raise Error

# Modelo
# ocurre un error
# raise Error