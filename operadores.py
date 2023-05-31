# OPERADORES UNÁRIO
# print("\n-----------------------\nOPERADORES UNÁRIO")

# print("Operador '~' : ", ~4)
# print("Operador '+' : ", +4)
# print("Operador '-' : ", -4)

meuInt = +3
meuInt = -meuInt
print(meuInt)

# OPERADOR ARITIMÉTRICO
print("\n-----------------------\nOPERADORES ARITIMÉTRICO")
X = 7
Y = 2

# print("Operador '+' : ", x+y)
# print("Operador '-' : ", x-y)
# print("Operador '*' : ", x*y)
# print("Operador '**' : ", x**y)
# print("Operador '/' : ", x/y)
# print("Operador '//' : ", x//y)
# print("Operador '%' : ", x%y)

print(((3 + 4) * 2) / 3)
print((2 ** 3 ** 2 * 2) // 2)
print(((3 + 4) * 2))
# OPERADORES RELACIONAIS
print("\n-----------------------\nOPERADORES RELACIONAIS")

x = 7
y = 2

# print("Op. Relacional x == y : ", x == y)
# print("Op. Relacional x != y : ", x != y)
# print('Op. Relacional x < y : ", x < y)
# print("Op. Relacional x > y : ", x > y)
# print("Op. Relacional x >= y : ", x >= y)
# print("Op. Relacional x <= y : ", x <= y)

# OPERADORES LÓGICOS
print("\n-----------------------\nOPERADORES LÓGICOS")

v = True
f = False

print("Op. lógicos v and f : ", v and f)
print("Op. lógicos v or f : ", v or f)
print("Op. lógicos v and not f : ", v and not f)

# OPERADORES DE ATRIBUIÇÃO
print("\n-----------------------\nOPERADORES ATRIBUIÇÃO")

print("Op. de Atribuição x = y ")
x = y
print("x: ", x)
print("y: ", y)

print("Op. de Atribuição x += y ")
x: int
x = x = y

x += y
print("x: ", x)
print("y: ", y)

# PRECEDÊNCIA DE OPERADORES
print("\n-----------------------\nPRECEDÊNCIA DE OPERADORES")

# 1. expoente e unario
print(-2 ** 2)
print(2 ** -2)

# 2 Aritméticos. primeiro divisões e mutiplicadores, depois + e -
print(1 + 3 / 3 * 1)

# 3 Depois de comparação, seguido de iguais
# print(False != 3 > 2)

# 4. por fim, operadores lógicos
# print(False != 3 > 2 and true)
# print((3 > 4) == True)
print(3 > 4 or 3 < 4)
print((not (3 > 4)) or (3 < 4))
print((not (3 > 4)) and (not (not (3 < 4))))
print((not (3 > 4)) and (False == (3 < 4)))
'''
x = 10
y = 20
3x += y + 3
y -= 2
y = z
var = z * 2
'''
print(5*"4",4)
