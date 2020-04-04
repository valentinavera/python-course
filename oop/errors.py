a, b = 10, 0
try:
  result = a/b # 1 línea o instrucción de error
except ZeroDivisionError as zerodiv:
  print(zerodiv)
  print("Ocurrió un error, no divida entre 0")
except (ArithmeticError, EnvironmentError) as e:
  print("..")
else:
  a = b
  b += 1
  print(result)
finally:
  print("Try terminado")

