import pygame as pg
import nivel_settings as ns

from jugador import Jugador
from suelo import Suelo

class Nivel1:
    def iniciar(self):
        pg.init()

        ventana = pg.display.set_mode((ns.ANCHO_NIVEL, ns.ALTO_NIVEL))
        pg.display.set_caption("Nivel1")

        # Estableciendo posición de inicio 
        jugador = Jugador(0, ns.ALTO_NIVEL-64)
        suelo = Suelo(0, ns.ALTO_NIVEL - 64)

        # Reloj para fps
        reloj = pg.time.Clock()

        # Bucle para mantener abierto el nivel
        running = True
        while running:

            reloj.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT: 
                    running = False

            ventana.fill(ns.BACKGROUND)
            
            teclas = pg.key.get_pressed()

            # Posiciones/Colisiones
            posicion_jugador = jugador.obtener_posicion()

            if jugador.hitbox.colliderect(suelo.rect):
                jugador.rect.y = suelo.rect.top - jugador.rect.height
                jugador.hitbox.center = jugador.rect.center

            jugador.mover(teclas)
            jugador.dibujar(ventana)
            
            suelo.dibujar(ventana)

            pg.display.update()

        pg.quit

Nivel1().iniciar()