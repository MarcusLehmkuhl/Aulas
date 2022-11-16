print("Alo mundo!")

# Quando quiser guardar uma String! (frase)
nome = "Marcus"
#Quando quiser guardar um número inteiro
idade = 20

#Exibir o meu nome (que está na variável nome)
print(nome)

#Quando quiser exibir a frase "Minha idade é " completando com o conteúdo da variável idade
#print("Meu nome é "+nome)
print("Minha idade é " + str(idade) + " anos")
print(f"Minha idade é {idade} anos")
print("Minha idade é {} anos".format(idade))

print("Meu nome é {} e tenho {} anos".format(nome, idade))
