# cadenas
mi_cadena = "Hola curso de python"
print(len(mi_cadena))
print(mi_cadena[6])
print(mi_cadena.index("r"))
print(mi_cadena[10 : 15])
print(mi_cadena.upper())
print(mi_cadena.lower())
print(mi_cadena.split("de"))

# formato de cadenas
formato = "Hoy es %s %d" % ("Viernes", 3)
print(formato)

formato = f"Hola {mi_cadena} {15}"
print(formato)

print("%.6f" % (10/3))
