import pygame as pg
from jugador import Jugador

pg.init()

window = pg.display.set_mode((800, 600))
pg.display.set_caption("Pantalla")

sprite_lautaro = pg.image.load

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()

pg.quit