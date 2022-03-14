import rsa

#para carregar um código rsa que não está no formato PEM ou DER em uma variavel, copie o código com número inteiro
#todos possuem 11 bytes de perda
#512 = 53 bytes
#1024 = 117 bytes
#2048 = 245 bytes
#4096 = 501 bytes
#8096 = 1013 bytes
class RsaGenerator ():

    public_server_key = bytes()
    private_server_key = bytes()

    #função que retorna novas chaves RSA
    def NewRSAKeys (rsa_max_bytes_size):
        rsa_max_bytes_size += 11
        (public_key, private_key) = rsa.newkeys(8 * rsa_max_bytes_size)
        return (public_key, private_key)

    #gera novas chaves e printa no console
    def PrintNewKeys (rsa_max_bytes_size):
        keys = RsaGenerator.NewRSAKeys(rsa_max_bytes_size)
        print("PUBLIC KEY PEM FORMAT:")
        print(rsa.PublicKey.save_pkcs1(keys[0], format = "PEM"))
        print("\n")
        print("PRIVATE KEY PEM FORMAT:")
        print(rsa.PrivateKey.save_pkcs1((keys[1]), format = "PEM"))
        print("\n")
        #print("PUBLIC KEY VARIABLE FORMAT:")
        #print(keys[0])
        #print("\n")
        #print("PRIVATE KEY VARIABLE FORMAT:")
        #print(keys[1])
        #print("\n")

    #usa a chave pública para encriptar uma mensagem
    def EncryptString (message_string, public_key):
        try:
            message_bytes = message_string.encode("utf-8")
            encrypted_message = rsa.encrypt(message_bytes, public_key)
            return encrypted_message
        except:
            return False

    #usa a chave privada para descriptar uma mensagem
    def DecryptBytes (the_bytes, private_key):
        try:
            decrypted_message = rsa.decrypt(the_bytes, private_key)
            return decrypted_message.decode("utf-8")
        except:
            return False