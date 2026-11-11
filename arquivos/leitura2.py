# arquivo em outra pasta, usar \\ ao dividir o caminho

try:
    arq = open("c:\\xampp\\xampp-control.ini", "r", encoding="utf-8")
    conteudo = arq.read()
    arq.close()
    print(conteudo)

except FileNotFoundError:
    print("Arquivo não encontrado.")