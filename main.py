
nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

#comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")
#exiba "Sua idade é ..."
print("Sua idade é {}".format(idade))

#e se eu quiser mostrar o dobro da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você é jovem ainda, jovem ainda...")


genero = input("Informe o gênero M=Masculino, F=Feminino, O=Outros: ")
if idade >= 18 and genero == "M":
  print("... e você também precisa/precisou prestar o serviço militar obrigatório")

