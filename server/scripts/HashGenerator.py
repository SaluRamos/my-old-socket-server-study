import uuid
from argon2 import PasswordHasher

class HashGenerator:

    #retorna o identificador único de uma string
    def GenerateUUID (the_string):
        return uuid.uuid5(namespace = uuid.NAMESPACE_X500, name = the_string)

    #retorna um identificador único aleatorio
    def GenerateRandomUUID ():
        return uuid.uuid4()
    
    #retorna o hash de uma string
    def GenerateHash (the_string, h = 64, s = 32, m = 16384, t = 4):
        password_hasher = PasswordHasher(hash_len = h, salt_len = s, memory_cost = m, time_cost = t)
        return password_hasher.hash(the_string)

    #verifica se o hash e a string batem
    def VerifyHash (the_string, the_hash):
        password_hasher = PasswordHasher()
        try:
            return password_hasher.verify(the_hash, the_string)
        except:
            return "False"