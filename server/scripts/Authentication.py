import sys

class Authentication ():

    def Login ():
        print("1 - verifica se o nickname ja foi cadastrado") #BinaryAlgorithSearch()
        print("2 - transforma a senha recebida em hash e compara com a senha do banco de dados")
        print("3 - gera um token de acesso e armazena no arquvio valid_tokens.txt")

    def VerifyLoginToken ():
        print("1 - compara o token recebido com os tokens do arquivo valid_tokens.txt")
        print("2 - verifica se o token ja expirou")

    def Register ():
        print("1 - verifica se os dados recebidos são válidos")
        print("2 - verifica se o número de celular já foi cadastrado") #BinaryAlgorithSearch()
        print("5 - armazena os dados para completar registros em to_register.txt")
        print("4 - envia token de verificação via whatsapp")

    def VerifyAccountViaCellPhone ():
        print("conta verificada")

    def RecuperationViaEmail ():
        pass
        #apenas por macs conhecidos!