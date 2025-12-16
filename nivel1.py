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
        jugador = Jugador(0, ns.ALTO_NIVEL -64 - 49)
        enemigos_pequenos = []
        
        for i in range(400, 1500, 200):
            enemigo = EnemigoPequeno(i, ns.ALTO_NIVEL - 64 -64)
            enemigos_pequenos.append(enemigo)

        suelo = Suelo(4)
        
        fondo_ancho = 2560
        fondo_alto = 480
        fondo = pg.Surface((fondo_ancho, fondo_alto))
        camara_x = 0
        
        for i in range(fondo_ancho // ns.ANCHO_NIVEL):
            sprite_fondo = pg.image.load("assets\\sprites_fondo\\fondo_prueba.png").convert()
            fondo.blit(sprite_fondo, (i * 640, 0))

        # Reloj para fps
        reloj = pg.time.Clock()

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

            ventana.blit(fondo, (camara_x, 0))
            camara_x = -jugador.hitbox.x + 300

            if camara_x >= 0:
                camara_x = 0
            if camara_x >= fondo_ancho - 64:
                camara_x = fondo_ancho - 64

            if jugador.rect.x <= 0:
                jugador.rect.x = 0
            if jugador.rect.x >= fondo_ancho - 64 - 300:
                jugador.rect.x = fondo_ancho - 64 - 300

            # Métodos Jugador
            jugador.movimiento(teclas)
            jugador.dibujar(ventana, camara_x)
            print(jugador.hitbox.center)
            # Métodos Enemigos
            for enemigo in enemigos_pequenos:
                if enemigo.vivo:
                    enemigo.dibujar(ventana, camara_x)
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
                                jugador.estadisticas["Vida"] += 10
                                if jugador.estadisticas["Vida"] > 100:
                                    jugador.estadisticas = 100
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
                    enemigos_pequenos.remove(enemigo)

            # Métodos Suelo
            suelo.dibujar_suelo(ventana, camara_x)

            for i in suelo.lista_suelos:
                if jugador.hitbox.colliderect(i):
                    jugador.restablecer_posicion(ns.ALTO_NIVEL -64 - 49)
            
            pg.display.update()

        pg.quit()

Nivel1().iniciar()