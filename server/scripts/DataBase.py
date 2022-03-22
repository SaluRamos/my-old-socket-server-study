from scripts.TimeClass import TimeClass

class Database:
    player = {
    "name":"", 
    "nickname":"", 
    "birthday":"", 
    "email":"", 
    "cellphone":"", 
    "password":"", 
    "country":"brasil", 
    "pix_key":"", 
    "fragments":0, 
    "registration_date":TimeClass.WhatTimeIsIt(time_depht = 4, end_char = False), #só adicionado quando 2fa celular for confirmado
    "reputation":0, 
    "pass_level":0,
    "crypto_loots":1,
    "crypto":0,
    "suitcase_loots":1,
    "lvl":1,
    "exp":0,
    "elo_wave":0.0,
    "elo_royale":0.0,
    "elo_team_pvp":0.0,
    "elo_ofa":0.0,
    "inv":[], #aponta para id da arma
    "skill_tree":{},
    "attributes":{},
    "friendlist":[],
    "macs":[], 
    "transactions":[] #aponta id das transações (compra e venda)
    }

    def DoBackup ():
        pass