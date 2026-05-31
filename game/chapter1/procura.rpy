


transform item_idle:
    easein .1 matrixcolor BrightnessMatrix(0)
    easein .1 zoom 1.0
    
transform item_hover:
    easein .1 zoom 1.2
    easein .1 matrixcolor BrightnessMatrix(0.15)

default procura_itens = {
    "butij": {
        "xpos": 501,
        "ypos": 912,
        "encontrado": False
    },
    "brink": {
        "xpos": 94,
        "ypos": 772,
        "encontrado": False
    },
    "comida": {
        "xpos": 1489,
        "ypos": 910,
        "encontrado": False
    },
    "phigi": {
        "xpos": 848,
        "ypos": 462,
        "encontrado": False
    },
    "dicio": {
        "xpos": 636,
        "ypos": 313,
        "encontrado": False
    },
    "gun": {
        "xpos": 850,
        "ypos": 977,
        "encontrado": False
    },
    "key": {
        "xpos": 1819,
        "ypos": 807,
        "encontrado": False
    },
    "mp": {
        "xpos": 1528,
        "ypos": 255,
        "encontrado": False
    },
    "sbt": {
        "xpos": 1342,
        "ypos": 645,
        "encontrado": False
    },
}

screen procura():
    for item in procura_itens:
        if not procura_itens[item]["encontrado"]:
            imagebutton:
                idle At(item, item_idle)
                hover At(item, item_hover)
                xpos procura_itens[item]['xpos']
                ypos procura_itens[item]['ypos']


                anchor (0.5, 0.5)
                activate_sound audio.collect
                action SetDict(procura_itens[item], "encontrado", True)

    if all(procura_itens[item]['encontrado'] for item in procura_itens):
        frame:
            xalign 0.5 yalign 0.5
            button:
                action Jump("pqp")
                text "{size=+100} ACHOU {/size}" style "button_text"



