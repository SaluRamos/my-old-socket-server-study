# -*- coding: utf-8 -*-
import random
from scripts.TimeClass import *

class TokenGenerator:
    
    fivebad_token_pool = [";", chr(92), "/", "'", '"', "="]
    numbers_token_pool = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    uuid_token_pool = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-"]
    letters_token_pool = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    simple_token_pool = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    semi_complex_token_pool = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ã", "â", "à", "á", "ê", "è", "é", "î", "ì", "í", "õ", "ô", "ò", "ó", "û", "ù", "ú", "Ã", "Â", "Á", "À", "Ê", "É", "È", "Î", "Í", "Ì", "Õ", "Ô", "Ó", "Ò", "Û", "Ú", "Ù", ".", "_", "~", ":", "@", "#", "$", "?", "ç", "Ç", "ý", "Ý", "ñ", "Ñ", "&", "%", "!", "|"]
    complex_token_pool = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ã", "â", "ä", "à", "á", "ê", "ë", "è", "é", "î", "ï", "ì", "í", "õ", "ô", "ö", "ò", "ó", "û", "ü", "ù", "ú", "Å", "Ã", "Â", "Ä", "Á", "À", "Ê", "Ë", "É", "È", "Î", "Ï", "Í", "Ì", "Õ", "Ö", "Ô", "Ó", "Ò", "Ü", "Û", "Ú", "Ù", ".", "_", "¯", "¨", "~", ":", "@", "#", "$", "?", "¿", "¥", "¢", "æ", "Æ", "ø", "Ø", "£", "×", "®", "©", "¤", "ð", "Ð", "ß", "µ", "¶", "§", "·", "ÿ", "ý", "Ý", "ç", "Ç", "ñ", "Ñ", "¬", "ƒ", "»", "«", "ª", "º", "¹", "²", "³", "°", "`", "´", "±", "÷", "½", "¾", "¼", "<", ">", "(", ")", "{", "}", "[", "]", "&", "|", "!", "¡", "+", "^", "*", "%", "-"]
    sick_token_pool = [chr(33) ,chr(34) ,chr(35) ,chr(36) ,chr(37) ,chr(38) ,chr(39) ,chr(40) ,chr(41) ,chr(42) ,chr(43) ,chr(44) ,chr(45) ,chr(46) ,chr(47) ,chr(48) ,chr(49) ,chr(50) ,chr(51) ,chr(52) ,chr(53) ,chr(54) ,chr(55) ,chr(56) ,chr(57) ,chr(58) ,chr(59) ,chr(60) ,chr(61) ,chr(62) ,chr(63) ,chr(64) ,chr(65) ,chr(66) ,chr(67) ,chr(68) ,chr(69) ,chr(70) ,chr(71) ,chr(72) ,chr(73) ,chr(74) ,chr(75) ,chr(76) ,chr(77) ,chr(78) ,chr(79) ,chr(80) ,chr(81) ,chr(82) ,chr(83) ,chr(84) ,chr(85) ,chr(86) ,chr(87) ,chr(88) ,chr(89) ,chr(90) ,chr(91) ,chr(92) ,chr(93) ,chr(94) ,chr(95) ,chr(96) ,chr(97) ,chr(98) ,chr(99) ,chr(100) ,chr(101) ,chr(102) ,chr(103) ,chr(104) ,chr(105) ,chr(106) ,chr(107) ,chr(108) ,chr(109) ,chr(110) ,chr(111) ,chr(112) ,chr(113) ,chr(114) ,chr(115) ,chr(116) ,chr(117) ,chr(118) ,chr(119) ,chr(120) ,chr(121) ,chr(122) ,chr(123) ,chr(124) ,chr(125) ,chr(126) ,chr(128) ,chr(129) ,chr(130) ,chr(131) ,chr(132) ,chr(133) ,chr(134) ,chr(135) ,chr(136) ,chr(137) ,chr(138) ,chr(139) ,chr(140) ,chr(141) ,chr(142) ,chr(143) ,chr(144) ,chr(145) ,chr(146) ,chr(147) ,chr(148) ,chr(149) ,chr(150) ,chr(151) ,chr(152) ,chr(153) ,chr(154) ,chr(155) ,chr(156) ,chr(157) ,chr(158) ,chr(159) ,chr(160) ,chr(161) ,chr(162) ,chr(163) ,chr(164) ,chr(165) ,chr(166) ,chr(167) ,chr(168) ,chr(169) ,chr(170) ,chr(171) ,chr(172) ,chr(173) ,chr(174) ,chr(175) ,chr(176) ,chr(177) ,chr(178) ,chr(179) ,chr(180) ,chr(181) ,chr(182) ,chr(183) ,chr(184) ,chr(185) ,chr(186) ,chr(187) ,chr(188) ,chr(189) ,chr(190) ,chr(191) ,chr(192) ,chr(193) ,chr(194) ,chr(195) ,chr(196) ,chr(197) ,chr(198) ,chr(199) ,chr(200) ,chr(201) ,chr(202) ,chr(203) ,chr(204) ,chr(205) ,chr(206) ,chr(207) ,chr(208) ,chr(209) ,chr(210) ,chr(211) ,chr(212) ,chr(213) ,chr(214) ,chr(215) ,chr(216) ,chr(217) ,chr(218) ,chr(219) ,chr(220) ,chr(221) ,chr(222) ,chr(223) ,chr(224) ,chr(225) ,chr(226) ,chr(227) ,chr(228) ,chr(229) ,chr(230) ,chr(231) ,chr(232) ,chr(233) ,chr(234) ,chr(235) ,chr(236) ,chr(237) ,chr(238) ,chr(239) ,chr(240) ,chr(241) ,chr(242) ,chr(243) ,chr(244) ,chr(245) ,chr(246) ,chr(247) ,chr(248) ,chr(249) ,chr(250) ,chr(251) ,chr(252) ,chr(253) ,chr(254) ,chr(255)]

    #retorna um token com tamanho especificado, time based ou não, tipos especificos de caracteres e time depht
    def GenerateRandomToken (pool_type, token_lenght = 6, bool_time_step = False, time_depht = 4, t_char = "-", t_char_end_time = True, t_char_in_time = False):
        system_time = ""
        if(bool_time_step == True):
            if(t_char_in_time == True):
                system_time = TimeClass.WhatTimeIsIt(time_depht = time_depht, t_char = t_char)
            else:
                system_time = TimeClass.WhatTimeIsIt(time_depht = time_depht, t_char = "")
            if(t_char_end_time == True and bool_time_step):
                system_time = system_time + t_char
        new_token = ""
        for i in range(1, token_lenght + 1, 1):
            new_token += pool_type[random.randrange(0, len(pool_type))]
        return (system_time + new_token)

    #adquirir o próximo token correspondente
    def NextToken (the_token, pool_type):
        int_cache = TokenGenerator.TokenToInt(the_token, pool_type)
        int_cache += 1
        return TokenGenerator.IntToToken(int_cache, pool_type)

    #adquirir o último token correspondente
    def LastToken (the_token, pool_type):
        int_cache = TokenGenerator.TokenToInt(the_token, pool_type)
        int_cache -= 1
        return TokenGenerator.IntToToken(int_cache, pool_type)

    #fragmentar int em um token
    def TokenToInt (the_token, pool_type):
        token_value = 0
        for i in range(0, len(the_token), 1):
            i_index = 0
            if(i == 0):
                i_index = pool_type.index(the_token[i])
            else:
                i_index = pool_type.index(the_token[i]) + 1
            if(i > 0):
                token_value += i_index * TokenGenerator.TokenPow(len(pool_type), i)
            else:
                token_value += i_index
        return token_value

    #função de potenciação especial (math impede qualquer x^n com n > 137)
    def TokenPow (base, expoent):
        int_cache = base
        for i in range(1, expoent, 1):
            int_cache = int_cache * base
        return int_cache
    
    #desfragmentar um token por distributiva
    def IntToToken (the_int, pool_type):
        string_cache = pool_type[0]
        token_lenght = 0
        #descobre tamanho do token que deve ser gerado
        for i in range(1, 1001, 1):
            if(TokenGenerator.TokenToInt(string_cache, pool_type) > the_int):
                token_lenght = i - 1
                break
            else:
                string_cache = string_cache + pool_type[0]
        the_token = []
        the_token[:0] = string_cache
        the_token.pop()
        #começa a testar os caracteres do token, do ultimo pro primeiro campo
        for i in range(token_lenght - 1, -1, -1):
            for w in range(len(pool_type) - 1, -1, -1):
                the_token[i] = pool_type[w]
                string_cache = "".join(the_token)
                if(TokenGenerator.TokenToInt(string_cache, pool_type) <= the_int):
                    break
        return "".join(the_token)

'''test = open(r"database/teste.db", "w")
for i in range(1, 10001, 1):
    test.write(TokenGenerator.GenerateRandomToken(token_lenght = random.randrange(180, 300), pool_type = TokenGenerator.simple_token_pool) + "\n")
test.close()'''