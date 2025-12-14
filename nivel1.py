import pygame as pg
import nivel_settings as ns

from jugador import Jugador
from enemigo import EnemigoPequeno
from suelo import Suelo

class Nivel1:

    def iniciar(self):
        pg.init()

        ventana = pg.display.set_mode((ns.ANCHO_NIVEL, ns.ALTO_NIVEL), pg.RESIZABLE)
        pg.display.set_caption("Nivel1")

        fondo = pg.Surface((1600, 1200))
        fondo.fill(ns.BACKGROUND)

        # Estableciendo posición de inicio 
        jugador = Jugador(100, ns.ALTO_NIVEL -64 - 49)
        enemigo = EnemigoPequeno(400, ns.ALTO_NIVEL -64 - 64)
        suelo = Suelo()
        camara = pg.Rect(0, 0, ns.ANCHO_NIVEL, ns.ALTO_NIVEL)

        # Reloj para fps
        reloj = pg.time.Clock()

        ESCALA_X = 1
        ESCALA_Y = 1

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
            
            if event.type == pg.VIDEORESIZE:
                ns.ANCHO_NIVEL, ns.ALTO_NIVEL = event.size
                ventana = pg.display.set_mode((ns.ANCHO_NIVEL, ns.ALTO_NIVEL), pg.RESIZABLE)
                ESCALA_X = ns.ANCHO_NIVEL / 640
                ESCALA_Y = ns.ALTO_NIVEL / 480

            ventana.fill(ns.BACKGROUND)
            
            jugador.rect.x = jugador.rect.x * ESCALA_X
            jugador.rect.y = jugador.rect.y * ESCALA_Y
            jugador.rect.width = int(jugador.rect.width * ESCALA_X)
            jugador.rect.height = int(jugador.rect.height * ESCALA_Y)

            jugador.hitbox.x = jugador.hitbox.x * ESCALA_X
            jugador.hitbox.y = jugador.hitbox.y * ESCALA_Y
            jugador.hitbox.width = int(jugador.hitbox.width * ESCALA_X)
            jugador.hitbox.height = int(jugador.hitbox.height * ESCALA_Y)

            teclas = pg.key.get_pressed()

            # Métodos Jugador
            jugador.movimiento(teclas)
            jugador.dibujar(ventana)
            #print(jugador.hitbox.center)

            # Métodos Enemigos
            enemigo.dibujar(ventana)
            enemigo.movimiento(jugador)

            # Métodos Suelo
            suelo.dibujar_suelo(ventana)

            for i in suelo.lista_suelos:
                if jugador.hitbox.colliderect(i):
                    jugador.restablecer_posicion(ns.ALTO_NIVEL -64 - 49)

            # Sistema colisión ataque jugador con enemigo
            if jugador.atacando and not jugador.tick_ataque:
                if jugador.ataque_hitbox.colliderect(enemigo.hitbox):
                    enemigo.estadisticas["Vida"] -= jugador.estadisticas["Daño"] 
                    print("Ataque conecto")
                    print(enemigo.estadisticas["Vida"])
                    if enemigo.estadisticas["Vida"] < 0:
                        print("Enemigo Muerto")
                    jugador.tick_ataque = True

            # Sistema colisión ataque enemigo con jugador
            if not jugador.dasheando:
                if enemigo.atacando and not enemigo.tick_ataque:
                    if enemigo.ataque_hitbox.colliderect(jugador.hitbox):
                        jugador.estadisticas["Vida"] -= enemigo.estadisticas["Daño"]
                        print("enemigo hizo daño")
                        enemigo.tick_ataque = True

            mover_camara(camara, jugador.hitbox.center)

            pg.display.update()

        pg.quit()

Nivel1().iniciar()