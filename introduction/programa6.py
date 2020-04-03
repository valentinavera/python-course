# diccionarios
diccionario = dict()
diccionario = {}
constantes = {
  "pi": 3.14,
  "e": 2.71
}
print(constantes)
constantes["g"] = 9.81
print(constantes)

print(constantes["g"])

print(constantes.keys())
print(constantes.values())

constantes["g"] = 10.1
print(constantes)

del constantes["g"]
print(constantes)
print(constantes["g"])