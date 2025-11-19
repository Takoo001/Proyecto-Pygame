import pygame as pg
from jugador import Jugador

pg.init()

window = pg.display.set_mode((800, 600))
pg.display.set_caption("Conceptos Básicos")

sprite_lautaro = pg.image.load

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    window.fill(background)

    # Dibujando figuras
    pg.draw.rect(window, light_blue, (150, 200, 100, 50))

    pg.display.update()

pg.quit