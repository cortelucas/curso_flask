# Principais listas compostas
# lista

# indices    0          1       2
cores = ["vermelho", "verde", "azul"]

numeros = [1, 2, 3]
misturas = [1, "Lucas", 4.5, True, cores, numeros, [1, 2, 3]]

cores.append("amArelo")
print(cores)
cores.insert(1, "branco")
print(cores)
cores.remove("azul")
print(cores)

# Tuplas
#                0           1        2
identidade = ("Lucas", "123456789-00", 27)

print(f"Nome é {identidade[0]}")
print(f"CPF é {identidade[1]}")
print(f"Idade é {identidade[2]}")

# desempacotamento
nome, cpf, idade = identidade
print(nome, cpf, idade)

# dicionario (object, array)
pessoa = {"nome": "Lucas", "cpf": "123456789-00", "idade": 27}
print(f"Olá, o {pessoa['nome']} tem {pessoa['idade']} anos.")

# Iteração (pegar um elemento de cada vez)

for cor in cores:
    print(cor.upper())

print("Gabriel"[0])
print("Gabriel"[-1])

for letra in "Gabriel":
    if letra == "i":
        continue
    print(letra)

# List Comprehension
print([letra for letra in "Gabriel"])

# list comprehension filtrada
print([letra for letra in "Gabriel" if letra != "i"])


for chave in pessoa:
    print(chave, ":", pessoa[chave])


for chave, valor in pessoa.items():
    print(chave, ":", valor)
