define personagem_base = dict(
    ctc="ctc",
    ctc_pause="ctc",
    ctc_position="fixed"
)


define l = Character(
    "   Lucas   ",
    image="prj",
    who_color="#f37a29",
    window_background="textbox/prjbox.png",
    **personagem_base
)

define n = Character(
    "   Nicolas   ",
    image="nico",
    who_color="#a270e4",
    window_background="textbox/nicobox.png",
    **personagem_base
)

define w = Character(
    "   Wallace   ",
    image="wllc",
    who_color="#50f173",
    window_background="textbox/wllcbox.png",
    **personagem_base
)

define p = Character(
    "   Poyo   ",
    image="poyo",
    who_color="#e66189",
    window_background="textbox/poyobox.png",
    **personagem_base
)

define d = Character(
    "   Dudu   ",
    image="dudu",
    who_color="#aba9b4",
    window_background="textbox/dudubox.png",
    **personagem_base
)

define q = Character(
    "   Queen   ",
    image="queen",
    who_color="#f73d3d",
    window_background="textbox/queenbox.png",
    **personagem_base
)

define t = Character(
    "   Theo   ",
    image="theo",
    who_color="#de0055",
    window_background="textbox/queenbox.png",
    **personagem_base
)
