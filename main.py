import sys

def cadastro(id):

  # Recebe os valores das variáveis de cadastro.
  print("*** Dentro da função ***")
  id = id
  n = input("Informe o nome: ")
  a = check_num(input("Informe a idade: "))
  e = input("Informe o e-mail: ")
  cpf = check_cpf(input("Digite o CPF (apenas números): "))

  return (id, n, a, e, cpf)  # Tuples. Immutable. Retorna um conjunto de parâmetros.


def imprime(data): # Old: n, a, e args.
  """
  Função para impressão de dados do cadastro.
    Entrada: dados cadastrais (nome, idade, email)
    Saída: nenhuma.
  """
  # Imprime os dados cadastrais na tela.
  print(f"*** Dados Cadastrais ***\
         \nCódigo: {data[0]}\
         \n\nNome: {data[1]}\
         \nIdade: {data[2]}\
         \nEmail: {data[3]}\
         \nCPF: {data[4]}\
         \n****************")

def check_cpf(unsanitizedCpf):

  cpf = unsanitizedCpf.replace(".", "")
  cpf = cpf.replace("-", "")
  # print(cpf)

  length_cpf = len(cpf)

  validFirstNum = False
  validSecondNum = False

  result = 0
  counter = 0

  # calc = result * 10 % 11

  # cpfNums = [] # One cannot append tuples.

  # for i in enumerate(length_cpf, start=0):
  #   cpfNums.append(cpf[i])

  # First Num.

  for i in range(length_cpf - 1, 1, -1):
    # print(i, cpf[counter])
    result += int(cpf[counter]) * i
    counter = counter + 1

  match result:
    case 10:
      result = 0

  if result * 10 % 11 == int(cpf[-2]):
    validFirstNum = True

  # print(result, cpf[-2])
###################################

  # Second Num.
  
  # result = None
  # Cleansing.
  result = 0
  counter = 0
  
  for j in range(length_cpf, 1, -1): # Non-pythonic.

    result += int(cpf[counter]) * j
    # print(cpf[counter])
    counter = counter + 1
    # print(j)
    # print(cpf)

  # print(result)
  match result:
    case 10:
      result = 0
      
  if result * 10 % 11 == int(cpf[-1]):
    validSecondNum = True
    # print(cpf[len(idx - 1)])
  
  if cpf.isnumeric() and length_cpf == 11 and validFirstNum and validSecondNum:

    # Python takes data types seriously. Each item needs to be a string, so it can be inserted later in the code.
    insertChars = [str(x) for x in str(cpf)] # A list comprehension. # cpf.split()
    
    insertChars.insert(3, ".")
    insertChars.insert(7, ".")
    insertChars[10] += "-" # Different syntax.
    
    cpf = "".join(insertChars)
    
    return cpf
    
  else:
    raise TypeError("Você deve digitar um CPF válido.")

def check_num(num):
  
  # valid = False
  
  if num.isnumeric(): # type(num) == int or type(num) == float:
    return num
    # pass
    # valid = True
  else:
    raise Exception("Você deve digitar números.")
    # sys.exit()

loop = True
count = 100

dataset = []

opt = -1

while opt != "3":
  print("\n*** Menu de Opções ***\
        \n1: Cadastro\
        \n2: Imprime dado\
        \n3: Sair")

  opt = input("\nDigite a opção desejada: ")
  print(f"Opção {opt} selecionada")

  if opt == '1': # Número é uma string no input.
    data = cadastro(len(dataset) + 1)
    dataset.append(data)
    # (n, a, e) = cadastro()
  elif opt == '2':
    if len(dataset) > 0:
      print("*** Menu de Exibição ***\
            \n1: Exibe um registro específico.\
            \n2: Imprime toda a base de dados.")
      opt_2 = input("Digite a opção: ")
      if opt_2 == "1":
        print("Imprime o registro desejado.")
        id = int(input("Digite o ID do registro: "))
        if id <= len(dataset):
          imprime(dataset[id-1])
        else:
          print("\nRegistro inexistente!")
      elif opt_2 == "2":
        
        for d in dataset:
          imprime(d)
      else:
        print("Opção Inválida.")
    
    else:
      print("Não existem dados para serem exibidos.")
  # imprime(n, a, e)
  else:
    print("Sistema Finalizado com Sucesso!")
    break

  # count = count - 1

# Utilizando a função cadastro para entrada de dado.
# name, age, email = cadastro()
# imprime(name, age, email)
# name2, age2, email2 = cadastro()
# imprime(name2, age2, email2)

# name3, age3, email3 = ""
# imprime(name3, age3, email3)

# print(f"Código principal\n\
# \nDados do cadastro: \
# \nNome: {name}\
# \nIdade: {age}\
# \nEmail: {email}")

# print(f"Código principal\n\
# \nDados do cadastro: \
# \nNome: {name2}\
# \nIdade: {age2}\
# \nEmail: {email2}")