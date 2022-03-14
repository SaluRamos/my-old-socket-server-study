import sys

class StringFilter:

    #verifica os caracteres de uma string através de uma whitelist
    def VerifyWhiteList (string_to_verify, white_list):
        characters = []
        characters[:0] = string_to_verify
        for i in characters:
            wrong_char = False
            for w in white_list:
                if(i == w):
                    wrong_char = True
                    break
            if(wrong_char == False):
                return False
        return True

    #verifica os caracteres de uma string através de uma blacklist
    def VerifyBlackList (string_to_verify, black_list):
        characters = []
        characters[:0] = string_to_verify
        for i in characters:
            for w in black_list:
                if(i == w):
                    return False
        return True

    #remove os caracteres mostrados
    def FilterBlackList (string_to_filter, black_list):
        characters = []
        characters[:0] = string_to_filter
        new_string = ""
        for i in characters:
            wrong_char = False
            for w in black_list:
                if(i == w):
                    wrong_char = True
                    break
            if(wrong_char == False):
                new_string += i
        return new_string