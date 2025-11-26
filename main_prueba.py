import pygame as pg

from jugador import Jugador

pg.init()

background = (30, 30, 30)

ventana = pg.display.set_mode((640, 480))
pg.display.set_caption("Prueba")

jugador = Jugador(0, 300)

reloj = pg.time.Clock()

running = True
while running:

    reloj.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False
    ventana.fill(background)

    teclas = pg.key.get_pressed()

    posición_ant_jugador = jugador.obtener_posicion()

    jugador.mover(teclas)

    ventana.fill(background)

    jugador.dibujar(ventana)

    pg.display.update()

pg.quit