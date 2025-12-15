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

        # Estableciendo posición de inicio 
        jugador = Jugador(100, ns.ALTO_NIVEL -64 - 49)
        enemigos_pequenos = []
        
        for i in range(400, 1500, 200):
            enemigo = EnemigoPequeno(i, ns.ALTO_NIVEL - 64 -64)
            enemigos_pequenos.append(enemigo)

        suelo = Suelo()
        
        fondo_ancho = 2560
        fondo_alto = 480
        fondo = pg.Surface((fondo_ancho, fondo_alto))
        
        for i in range(fondo_ancho // ns.ANCHO_NIVEL):
            sprite_fondo = pg.image.load("assets\\sprites_fondo\\fondo_prueba.png").convert()
            fondo.blit(sprite_fondo, (i * 640, 0))

        camara = pg.Rect(0, 0, ns.ANCHO_NIVEL, ns.ALTO_NIVEL)

        # Reloj para fps
        reloj = pg.time.Clock()

        ESCALA_X = 1
        ESCALA_Y = 1

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

            ventana.fill(ns.BACKGROUND)

            teclas = pg.key.get_pressed()

            # Métodos Jugador
            jugador.movimiento(teclas)
            jugador.dibujar(ventana)
            #print(jugador.hitbox.center)

            # Métodos Enemigos
            for enemigo in enemigos_pequenos:
                if enemigo.vivo:
                    enemigo.dibujar(ventana)
                    enemigo.movimiento(jugador)

                    # Sistema colisión ataque jugador con enemigo
                    if jugador.atacando and not jugador.tick_ataque:
                        if jugador.ataque_hitbox.colliderect(enemigo.hitbox):
                            enemigo.estadisticas["Vida"] -= jugador.estadisticas["Daño"] 
                            print("Ataque conecto")
                            print(enemigo.estadisticas["Vida"])
                            enemigo.tick_dano_recibido = True

                            if enemigo.estadisticas["Vida"] <= 0:
                                print("Enemigo Muerto")
                                enemigo.vivo = False
                                jugador.estadisticas["Vida"] += 5
                            jugador.tick_ataque = True

                    # Sistema colisión ataque enemigo con jugador
                    if not jugador.dasheando:
                        if enemigo.atacando and not enemigo.tick_ataque:
                            if enemigo.ataque_hitbox.colliderect(jugador.hitbox):
                                jugador.estadisticas["Vida"] -= enemigo.estadisticas["Daño"]
                                print("enemigo hizo daño")
                                enemigo.tick_ataque = True
                else:
                    enemigo.muerto()

            # Métodos Suelo
            suelo.dibujar_suelo(ventana)

            if jugador.hitbox.right > camara.right - 50:
                camara.x = jugador.hitbox.right - ns.ANCHO_NIVEL + 50
            if jugador.hitbox.left < camara.left + 50:
                camara.x = jugador.hitbox.left - 50

            camara.x = max(0, min(camara.x, fondo_ancho - ns.ANCHO_NIVEL))

            for i in suelo.lista_suelos:
                if jugador.hitbox.colliderect(i):
                    jugador.restablecer_posicion(ns.ALTO_NIVEL -64 - 49)
                        
            pg.display.update()

        pg.quit()

Nivel1().iniciar()