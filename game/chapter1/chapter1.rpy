# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show prj

    # These display lines of dialogue.

    l "You've created a new Ren'Py game."
    l "[procura_itens['butij']['encontrado']]"
    scene procure
    call screen procura
    

    l "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

label pqp:
    l "MDS TO COM MT TESAO"

    return
