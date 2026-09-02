dados = ['tronco','folha','caule','tronco','galho','flor','tronco']
print(dados)

dados.remove('tronco') # só remove a primeira ocorrêmcia
print(dados)

while 'tronco' in dados : dados.remove('tronco') # use um laço para
                                                 # remover todos
print(dados)
