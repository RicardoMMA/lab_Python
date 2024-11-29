palabra1 = input("Digite una palabra: ")
palabra2 = input("Digite la segunda palabra: ")

if palabra1.endswith(palabra2):
    print(f'"{palabra2}" es sufijo de la palabra "{palabra1}".')
else:
    print(f'"{palabra2}" no es sufijo de la palabra "{palabra1}".')
