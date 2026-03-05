# pedir numero
numero = input("Ingrese un número de 4 dígitos: ")

# verificar si tiene 4 dígitos
if len(numero) == 4:

    # separar los dígitos
    a = int(numero[0])
    b = int(numero[1])
    c = int(numero[2])
    d = int(numero[3])

    # ordenar ascendente
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b
    if c > d:
        c, d = d, c

    print("Ascendente:", a, b, c, d)
    print("Descendente:", d, c, b, a)

else:
    print("Número no válido, debe tener 4 dígitos")