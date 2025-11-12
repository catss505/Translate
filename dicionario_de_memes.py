import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Es una risa que se puede referir a algo gracioso",
            "XD": "Es un emoticono que expresa una risa",
            "LMAO": "Significa que se parte el culo en pocas palabras",
            "UWU": "Es un emoticono de una cara",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado"
            }

while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print( meme_dict[word])
    else:
        print("Tu palabra no se encuentra en el dicionario")
    time.sleep(2)
