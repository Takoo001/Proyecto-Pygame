import pygame as pg
import nivel_settings as ns

from jugador import Jugador
from enemigo import EnemigoPequeno
from suelo import Suelo

class Nivel1:

    def iniciar(self):
        pg.init()

        ventana = pg.display.set_mode((ns.ANCHO_NIVEL, ns.ALTO_NIVEL))
        pg.display.set_caption("Nivel1")

        # Estableciendo posición de inicio 
        jugador = Jugador(0, ns.ALTO_NIVEL -64 - 49)
        enemigos_pequenos = []

        largo_mapa = 6

        suelo = Suelo(largo_mapa)
        
        fondo_ancho = 640 * largo_mapa
        fondo_alto = 480
        fondo = pg.Surface((fondo_ancho, fondo_alto))
        camara_x = 0
    
        for i in range(400, fondo_ancho, 400):
            enemigo = EnemigoPequeno(i, ns.ALTO_NIVEL - 64 -64)
            enemigos_pequenos.append(enemigo)

        for i in range(fondo_ancho // ns.ANCHO_NIVEL):
            sprite_fondo = pg.image.load("assets\\sprites_fondo\\ia_4.png").convert()
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

            ventana.fill(ns.BACKGROUND)
            teclas = pg.key.get_pressed()

            ventana.blit(fondo, (camara_x, 0))
            camara_x = (-jugador.rect.x + 300)

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
            jugador.dibujar_corazones(ventana)

            print(jugador.vida)
            # Métodos Enemigos
            for enemigo in enemigos_pequenos:
                if enemigo.vivo:
                    enemigo.dibujar(ventana, camara_x)
                    enemigo.movimiento(jugador)

                    # Sistema colisión ataque jugador con enemigo
                    if jugador.atacando and not jugador.tick_ataque:
                        if jugador.ataque_hitbox.colliderect(enemigo.hitbox):
                            enemigo.vida -= jugador.dano             
                            print("Ataque conecto")
                            print(enemigo.vida)
                            enemigo.tick_dano_recibido = True

                            if enemigo.vida <= 0:
                                print("Enemigo Muerto")
                                enemigo.vivo = False
                                jugador.vida += 20
                                if jugador.vida > 100:
                                    jugador.vida = 100
                            jugador.tick_ataque = True

                    # Sistema colisión ataque enemigo con jugador
                    if not jugador.dasheando:
                        if enemigo.atacando and not enemigo.tick_ataque:
                            if enemigo.ataque_hitbox.colliderect(jugador.hitbox):
                                jugador.vida -= enemigo.dano
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