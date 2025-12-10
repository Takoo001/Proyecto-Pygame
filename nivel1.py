import pygame as pg
import nivel_settings as ns

from jugador import Jugador
from suelo import Suelo

class Nivel1:

    def iniciar(self):
        pg.init()

        ventana = pg.display.set_mode((ns.ANCHO_NIVEL, ns.ALTO_NIVEL))
        pg.display.set_caption("Nivel1")

        fondo = pg.Surface((1600, 1200))
        fondo.fill(ns.BACKGROUND)

        # Estableciendo posición de inicio 
        jugador = Jugador(100, ns.ALTO_NIVEL -64 - 49)
        suelo = Suelo()
        camara = pg.Rect(0, 0, ns.ANCHO_NIVEL, ns.ALTO_NIVEL)

        # Reloj para fps
        reloj = pg.time.Clock()

        def mover_camara(camara, jugador):
            camara.center = jugador
            camara.x = max(0, min(camara.x, fondo.get_width() - camara.width))
            camara.y = max(0, min(camara.y, fondo.get_height() - camara.height))

        # Bucle para mantener abierto el nivel
        running = True
        while running:

            reloj.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT: 
                    running = False

            ventana.fill(ns.BACKGROUND)
            
            teclas = pg.key.get_pressed()

            posicion_jugador = jugador.obtener_posicion()

            jugador.movimiento(teclas, ventana)
            jugador.dibujar(ventana)

            print(jugador.hitbox.center)
            suelo.dibujar_suelo(ventana)
            for i in suelo.lista_suelos:
                if jugador.hitbox.colliderect(i):
                    jugador.restablecer_posicion(ns.ALTO_NIVEL -64 - 49)

            mover_camara(camara, jugador.hitbox.center)

            pg.display.update()

        pg.quit()

Nivel1().iniciar()