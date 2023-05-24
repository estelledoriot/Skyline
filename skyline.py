"""Animation Skyline
Génère une skyline aléatoire avec des bâtiments, des paysages ...
"""

import turtle
from math import atan, cos, pi, sqrt
from random import choice, randint

# ******************************************************************************
# *                               Utilitaire                                   *
# ******************************************************************************


def centrer_affichage():
    """fait défiler le décors"""

    x, y = turtle.getturtle().position()
    largeur = turtle.getscreen().window_width()
    hauteur = turtle.getscreen().window_height()
    turtle.setworldcoordinates(
        x - largeur / 2, y - 30, x + largeur / 2, y + hauteur - 30
    )


# ******************************************************************************
# *                               Végétation                                   *
# ******************************************************************************


def sapin():
    """dessine un sapin"""

    lf = randint(10, 20)
    ht = randint(20, 30)
    lt = randint(7, 12)
    hf = randint(50, 100)
    a = 180 / pi * atan(hf / (lf + lt / 2))
    d = sqrt(hf**2 + (lf + lt / 2) ** 2)

    # sol
    turtle.setheading(0)
    turtle.forward(lf)
    turtle.left(90)
    # tronc
    turtle.forward(ht)
    turtle.left(90)
    # cône
    turtle.forward(lf)
    turtle.right(180 - a)
    turtle.forward(d)
    turtle.right(2 * a)
    turtle.forward(d)
    turtle.right(180 - a)
    turtle.forward(lf)
    # tronc
    turtle.left(90)
    turtle.forward(ht)
    # sol
    turtle.left(90)
    turtle.forward(lf)


def chene():
    """dessine un chêne"""

    lt = randint(7, 12)
    ht = randint(20, 30)
    rf = randint(15, 40)
    a = 180 / pi * atan(lt / (2 * rf))

    # sol
    turtle.setheading(0)
    turtle.forward(rf - 5)
    turtle.left(90)
    # tronc
    turtle.forward(ht)
    # feuillage
    turtle.left(90 - a)
    turtle.circle(-rf, 360 - 2 * a)
    turtle.left(90 - a)
    # tronc
    turtle.forward(ht)
    # sol
    turtle.left(90)
    turtle.forward(rf - 5)


def marronnier():
    """dessine un marronnier"""

    lfb = randint(10, 20)
    ht = randint(20, 30)
    lt = randint(7, 12)
    hf = randint(40, 70)
    lfh = randint(lt // 2 + 1, lfb + lt // 2 - 1)
    a = 180 / pi * atan(hf / (lfb + lt / 2 - lfh))
    d = sqrt(hf**2 + (lfb + lt / 2 - lfh) ** 2)

    # sol
    turtle.setheading(0)
    turtle.forward(lfb)
    turtle.left(90)
    # tronc
    turtle.forward(ht)
    turtle.left(90)
    # cône
    turtle.forward(lfb)
    turtle.right(180 - a)
    turtle.forward(d)
    turtle.right(a)
    turtle.forward(2 * lfh)
    turtle.right(a)
    turtle.forward(d)
    turtle.right(180 - a)
    turtle.forward(lfb)
    # tronc
    turtle.left(90)
    turtle.forward(ht)
    # sol
    turtle.left(90)
    turtle.forward(lfb)


# ******************************************************************************
# *                                Terrains                                    *
# ******************************************************************************


def eau():
    """dessine une étendue d'eau"""

    turtle.setheading(-90)
    turtle.circle(10, 60)
    for _ in range(randint(5, 12)):
        turtle.setheading(0)
        turtle.circle(10, 160)
        turtle.right(170)
        turtle.circle(-20, 80)
    turtle.setheading(0)
    turtle.circle(10, 160)
    turtle.right(170)
    turtle.circle(-20, 40)


def plaine():
    """dessine une plaine"""

    for _ in range(randint(1, 2)):
        turtle.setheading(randint(0, 15))
        turtle.forward(randint(20, 50))
        turtle.setheading(randint(-15, 0))
        turtle.forward(randint(20, 50))


def montagne():
    """dessine une montagne"""

    for _ in range(randint(8, 15)):
        turtle.setheading(randint(10, 60))
        turtle.forward(randint(10, 30))
    turtle.setheading(0)
    turtle.forward(randint(3, 5))
    for _ in range(randint(5, 10)):
        turtle.setheading(randint(-60, -10))
        turtle.forward(randint(10, 30))
    turtle.setheading(0)
    turtle.forward(randint(7, 10))


# ******************************************************************************
# *                               Bâtiments                                    *
# ******************************************************************************


def maison():
    """dessine une maison"""

    hauteur = randint(15, 40)
    largeur = randint(25, 45)
    toit = randint(8, largeur // 2)

    # bord
    turtle.setheading(0)
    turtle.forward(10)
    turtle.left(90)
    # mur
    turtle.forward(hauteur)
    turtle.left(90)
    # toit
    turtle.forward(3)
    turtle.right(135)
    turtle.forward(toit / cos(pi / 8))
    turtle.right(45)
    turtle.forward(largeur - 2 * toit)
    turtle.right(45)
    turtle.forward(toit / cos(pi / 8))
    turtle.right(135)
    turtle.forward(3)
    # mur
    turtle.left(90)
    turtle.forward(hauteur)
    # bord
    turtle.left(90)
    turtle.forward(10)


def immeuble():
    """dessine un immeuble"""

    hauteur = randint(100, 300)
    largeur = randint(65, 75)

    # bord
    turtle.setheading(0)
    turtle.forward(10)
    turtle.left(90)
    # mur
    turtle.forward(hauteur)
    turtle.right(90)
    # toit
    turtle.forward(largeur)
    # mur
    turtle.right(90)
    turtle.forward(hauteur)
    # bord
    turtle.left(90)
    turtle.forward(10)


def gratte_ciel():
    """dessine un gratte-ciel"""

    def dessiner_murs(cote, hauteur):
        reste = hauteur
        for _ in range(randint(1, 3)):
            avance = randint(0, reste)
            turtle.forward(avance)
            reste -= avance
            turtle.right(90 * cote)
            turtle.forward(randint(5, 12))
            turtle.left(90 * cote)
        turtle.forward(reste)

    hauteur = randint(400, 600)
    largeur = randint(65, 85)
    gauche = 1
    droite = -1

    # bord
    turtle.setheading(0)
    turtle.forward(10)
    turtle.left(90)
    # mur
    dessiner_murs(gauche, hauteur)
    # toit
    turtle.right(90)
    turtle.forward(largeur)
    turtle.right(90)
    # mur
    dessiner_murs(droite, hauteur)
    # bord
    turtle.left(90)
    turtle.forward(10)


def tour_eiffel():
    """dessine une tour Eiffel"""

    d1 = 80
    d2 = 50
    d3 = 150
    d4 = 10
    a1 = 50
    a2 = 15
    a3 = 15
    a4 = 40
    r = (
        d1 * cos(a1 * pi / 180)
        + d2 * cos((a1 + a2) * pi / 180)
        + d3 * cos((a1 + a2 + a3) * pi / 180)
        + d4 * cos((a1 + a2 + a3 - a4) * pi / 180)
    )
    delta = 50
    delta2 = delta * cos(20 * pi / 180)
    x0 = turtle.xcor()

    # sol
    turtle.setheading(0)
    turtle.forward(20)
    # premier étage
    turtle.left(a1)
    turtle.forward(d1)
    x1 = turtle.xcor()
    y1 = turtle.ycor()
    # deuxième étage
    turtle.left(a2)
    turtle.forward(d2)
    x2 = turtle.xcor()
    y2 = turtle.ycor()
    # troisième étage
    turtle.left(a3)
    turtle.forward(d3)
    # pointe
    turtle.right(a4)
    turtle.forward(d4)
    turtle.left(50)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(20)
    turtle.left(50)
    turtle.forward(d4)
    turtle.right(a4)
    # troisième étage
    turtle.forward(d3)
    turtle.left(a3)
    # deuxième étage
    x3 = turtle.xcor()
    y3 = turtle.ycor()
    turtle.forward(d2)
    turtle.left(a2)
    # premier étage
    x4 = turtle.xcor()
    y4 = turtle.ycor()
    turtle.forward(d1)
    turtle.left(a1)
    # sol
    turtle.forward(20)
    x = turtle.xcor()
    y = turtle.ycor()

    # pieds
    turtle.penup()
    turtle.setx(x0 + 20 + (1 - cos(20 * pi / 180)) * r + delta2)
    turtle.pendown()
    turtle.setheading(70)
    turtle.circle(-r + delta, 140)
    turtle.penup()

    # espace
    turtle.goto(x1 + 20, y1)
    turtle.pendown()
    turtle.goto(x2 + 20, y2)
    turtle.goto(x3 - 20, y3)
    turtle.goto(x4 - 20, y4)
    turtle.goto(x1 + 20, y1)
    turtle.penup()

    # repositionnement
    turtle.goto(x, y)
    turtle.pendown()


turtle.mode("world")
turtle.screensize(1000, 500)
turtle.bgcolor("navy blue")
turtle.color("white")


elements_decor = {
    "construction": [maison, immeuble, gratte_ciel, tour_eiffel],
    "terrain": [eau, montagne, plaine],
    "vegetation": [sapin, chene, marronnier],
}

centrer_affichage()

while True:
    nom_element = choice(list(elements_decor.keys()))
    if nom_element == "terrain":
        element_decor = choice(elements_decor[nom_element])
        element_decor()
        centrer_affichage()
    else:
        for _ in range(3, 8):
            element_decor = choice(elements_decor[nom_element])
            element_decor()
            centrer_affichage()
