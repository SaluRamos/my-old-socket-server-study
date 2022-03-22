from Crypto.Cipher import AES
from TokenGenerator import TokenGenerator

class AesGenerator:

    def EncryptString (the_key, the_data):
        cipher = AES.new(key = the_key, mode = AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(bytes(the_data, encoding = "utf-8"))
        print(ciphertext)
        return (ciphertext, cipher.nonce)

    def DecryptBytes (the_key, the_cipher, the_nonce):
        cipher = AES.new(key = the_key, mode = AES.MODE_GCM, nonce = the_nonce)
        return cipher.decrypt(the_cipher).decode("utf-8")

    #aceita keys de 16, 24 e 32 bytes
    def GenerateAesKey (the_lenght):
        if(the_lenght != 16 and the_lenght != 24 and the_lenght != 32):
            return "ERROR"
        return bytes(TokenGenerator.GenerateRandomToken(pool_type = TokenGenerator.simple_token_pool, token_lenght = the_lenght), encoding = "utf-8")

teste = AesGenerator.GenerateAesKey(32)
encrypted = AesGenerator.EncryptString(teste, the_data = "aaaaaaaaaaaaaaaasadafawdddddddaaaaaaa")
print(AesGenerator.DecryptBytes(the_key = teste,the_cipher = encrypted[0],the_nonce = encrypted[1]))
