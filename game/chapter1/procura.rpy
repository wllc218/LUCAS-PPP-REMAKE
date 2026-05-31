

transform item_anim:
    on hover:
        ease .1 zoom 1.2
        easein .1 matrixcolor BrightnessMatrix(0.15)

    on idle:
        ease .1 zoom 1.0
        easein .1 matrixcolor BrightnessMatrix(0)

transform item_coletado:
    ease 0.2 zoom 0 rotate 360
   
        

default procura_itens = {
    "butij": {
        "xpos": 501,
        "ypos": 912,
        "encontrado": False,
        "coletando": False
    },
    "brink": {
        "xpos": 94,
        "ypos": 772,
        "encontrado": False,
        "coletando": False
    },
    "comida": {
        "xpos": 1489,
        "ypos": 910,
        "encontrado": False,
        "coletando": False
    },
    "phigi": {
        "xpos": 848,
        "ypos": 462,
        "encontrado": False,
        "coletando": False
    },
    "dicio": {
        "xpos": 636,
        "ypos": 313,
        "encontrado": False,
        "coletando": False
    },
    "gun": {
        "xpos": 850,
        "ypos": 977,
        "encontrado": False,
        "coletando": False
    },
    "key": {
        "xpos": 1819,
        "ypos": 807,
        "encontrado": False,
        "coletando": False
    },
    "mp": {
        "xpos": 1528,
        "ypos": 255,
        "encontrado": False,
        "coletando": False
    },
    "sbt": {
        "xpos": 1342,
        "ypos": 645,
        "encontrado": False,
        "coletando": False
    },
}

screen procura():
    frame:
        xalign 0.1
        yalign 0.1
        background "#0000008f"
        padding (20, 20)

        vbox:
            text "Butijão " + ("✅" if procura_itens["butij"]["encontrado"] else "")
            text "Brinquedos Sexuais " + ("✅" if procura_itens["brink"]["encontrado"] else "")
            text "Comida " + ("✅" if procura_itens["comida"]["encontrado"] else "")
            text "Papel higiênico " + ("✅" if procura_itens["phigi"]["encontrado"] else "")
            text "Dicionário " + ("✅" if procura_itens["dicio"]["encontrado"] else "")
            text "Arma " + ("✅" if procura_itens["gun"]["encontrado"] else "")
            text "Máscara de Pedra " + ("✅" if procura_itens["mp"]["encontrado"] else "")
            text "Sapatos Brawl Stars " + ("✅" if procura_itens["sbt"]["encontrado"] else "")



    for item in procura_itens:
        if not procura_itens[item]["encontrado"]:
            if procura_itens[item]["coletando"]:
                add item:
                    at item_coletado

                    xpos procura_itens[item]["xpos"]
                    ypos procura_itens[item]["ypos"]
                    anchor (0.5, 0.5)
                    
                timer 1.8 action [
                    SetDict(procura_itens[item], "encontrado", True),
                    SetDict(procura_itens[item], "coletando", False),

                ]
                add "explosao" at Transform(
                    xpos=procura_itens[item]["xpos"],
                    ypos=procura_itens[item]["ypos"],
                    xanchor=0.5,
                    yanchor=0.5,
                    zoom=2.0
                )
        

            else:
                imagebutton:
                    idle item
                    hover item
                    at item_anim

                    xpos procura_itens[item]['xpos']
                    ypos procura_itens[item]['ypos']

                    anchor (0.5, 0.5)

                    activate_sound audio.collect

                    action SetDict(procura_itens[item], "coletando", True)
    if all(procura_itens[item]['encontrado'] for item in procura_itens):
        frame:
            xalign 0.5 yalign 0.5
            button:
                action Jump("pqp")
                text "{size=+100} ACHOU {/size}" style "button_text"



