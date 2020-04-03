# PEP8
# ISO 29110

"""
Esto es una docstring del programa.
"""

def cifrar(texto_claro, clave='C'):
  alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  indice_clave = alfabeto.index(clave)
  resultado = ''
  for letra in texto_claro:
    if letra in alfabeto:
      indice = (alfabeto.index(letra) + indice_clave) % len(alfabeto)
      resultado += alfabeto[indice]
    else:
      resultado += letra
  return resultado


texto = 'I AM YOUR FATHER'
key = 'H'
resultado = cifrar(texto)
print(resultado)
