# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen", color="#34f034")
#define m = Character("Me", color="#cf522c")

define e = Character(None, image="Eileen", kind=bubble)
define m = Character(None, image="Me", kind=bubble)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/bgsound.mp3"
    scene bg
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen at right

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    show me at left

    m "These are my first changes:"

    m "I added a new character, pictures and colors for both of them, and a new background."

    m "Later I added transition effects and audio."

    hide eileen
    hide me
    with dissolve
    stop music

    # This ends the game.

    return
