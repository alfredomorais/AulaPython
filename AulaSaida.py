nome = "Alfredo"
sobrenome = "Morais"
print("Nome",nome+" "+sobrenome, sep=': ')
'''
i = 1
while 1:
    if i %2 == 0:
        break
        print(i)
       i += 2
'''
#numero = int(input("digite um numero"))
#print(numero + 50)
arquivo = open("venv/ARQUIVO.txt", "w")
print("print no arquivo", file=arquivo)
arquivo.close()
'''
arquivo = open("arquivo.txt","r")
print("print no arquivo", file=arquivo)
arquivo.close()
'''
'''
s  =0
i = 0
n = 10
while i<n:
    if i > n // 3:
        s+=i
        i+=1
    else:
        print(i,s)
'''
'''
i = 1
while 1:
    if i % 2 == 0:
        break
        print(i)
        i+=2
        print(i)
'''

