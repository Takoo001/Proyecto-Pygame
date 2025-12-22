import pygame as pg
from entidad import Entidad
import random as rd

class Enemigo(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.vida = 50
        self.dano = 2
        self.velocidad = rd.randint(1, 2)

        self.cooldown = 1000
        self.ultimo_ataque = 0

        self.hitbox = pg.Rect(self.x, self.y, 64, 64)
        self.ataque_hitbox = pg.Rect(self.rect.centerx, self.rect.centery, 64, 64)

        self.frame_milisegundos = 100
        self.frame_milisegundos_ataque = 10

        self.tiempo_de_inicio = pg.time.get_ticks()

        if len(self.frames_ataque) > 0:
            self.imagen_ataque = self.frames_ataque[0]

    def movimiento(self, jugador):
        tiempo_actual = pg.time.get_ticks()

        mov_x = 0

        if self.hitbox.centerx > jugador.hitbox.centerx + 60:
            mov_x -= self.velocidad
            self.direccion = "IZQUIERDA"
            self.flip = True

        elif self.hitbox.centerx < jugador.hitbox.centerx - 60:
            mov_x += self.velocidad
            self.direccion = "DERECHA"
            self.flip = False

        if self.direccion == "DERECHA":
            self.ataque_hitbox = pg.Rect(self.rect.centerx + 15, self.rect.centery - 32, 64, 64)
        else:
            self.ataque_hitbox = pg.Rect(self.rect.centerx - 79, self.rect.centery - 32, 64, 64)

        if self.ataque_hitbox.colliderect(jugador.hitbox):
            if tiempo_actual - self.ultimo_ataque > self.cooldown:
                jugador.vida -= self.dano
                self.ultimo_ataque = tiempo_actual
                self.atacando = True

        self.rect.x += mov_x
        self.hitbox.center = self.rect.center

        if self.atacando:
            self.animar_ataque()

        if mov_x != 0:
            self.animar_corriendo()
        else:
            self.imagen = self.sprite_quieto

class EnemigoPequeno(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Sprites de Enemigo Pequeño
        self.sprite_quieto = pg.image.load("assets/sprites/sprites_enemigos/español_pequeño_quieto.png").convert_alpha()
        self.sprite_corriendo = pg.image.load("assets/sprites/sprites_enemigos/español_pequeño_corriendo.png").convert_alpha()
        self.sprite_ataque = pg.image.load("assets/sprites/sprites_enemigos/ataque_español_pequeño.png").convert_alpha()

        # Sprites
        self.frames_corriendo = self.recortar_frames(self.sprite_corriendo, 9, 64, 64)
        self.frames_ataque = self.recortar_frames(self.sprite_ataque, 12, 64, 64)

        # Modificando cooldown de ataque y rapidez de frames
        self.cooldown = 4000
        self.frame_milisegundos_ataque = 50

        self.hitbox = pg.Rect(self.x, self.y, 28, 58)
        self.ataque_hitbox = pg.Rect(self.rect.centerx + 15, self.rect.centery, 64, 64)