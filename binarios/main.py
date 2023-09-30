from ctypes import sizeof
import io
import pickle

class Contato:
  def __init__(self, nome, telefone, email):
    self.nome = nome
    self.telefone = telefone
    self.email = email

def escrever_contato(arquivo, contato):
  contato_dict = contato.__dict__
  contato_bytes = pickle.dumps(contato_dict)
  arquivo.write(contato_bytes)

def ler_contato(arquivo):
  contato_bytes = arquivo.read(sizeof(Contato.__dict__))
  contato_dict = pickle.loads(contato_bytes)
  contato = Contato(**contato_dict)
  return contato

def main():
  arquivo = io.open("contatos.bin", "wb")

  while True:
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = Contato(nome, telefone, email)
    escrever_contato(arquivo, contato)

    opcao = input("Deseja inserir outro contato? (1 - Sim | 2 - Não): ")
    if opcao == "2":
      break

  arquivo.close()

if __name__ == "__main__":
  main()