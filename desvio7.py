# programa de login (usando operador lógico AND)
import getpass

usu = input("Usuário: ")
sen = getpass.getpass("Senha: ")

if usu == "admin" and sen == "9876" :
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO.")
    


