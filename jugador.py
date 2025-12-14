import pygame as pg
import nivel_settings as ns
from entidad import Entidad

class Jugador(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Sprites
        self.flip = False
        self.quieto = pg.image.load("assets\sprites_lautaro\Lautaro_base64.png").convert_alpha()
        self.sprite_corriendo = pg.image.load("assets\sprites_lautaro\lautaro_corriendo.png").convert_alpha()
        self.sprite_ataque = pg.image.load("assets\\sprites_lautaro\\ataque_prueba.png").convert_alpha()
        self.girando = pg.image.load("assets\sprites_lautaro\giro_aire.png").convert_alpha()

        # Recorte sprites por sus frames
        self.frames_corriendo = self.recortar_frames(self.sprite_corriendo, 12, 64, 64)
        self.frames_ataque = self.recortar_frames(self.sprite_ataque, 7, 64, 64)
        self.frames_girando = self.recortar_frames(self.girando, 4, 64, 64)

        # Posición Hitbox

        # Frames de Sprites Corriendo
        self.frame_corriendo = 0
        self.frame_tiempo_corriendo = 0
        self.frame_milisegundos_corriendo = 100

        # Frames de Sprite Atacando
        self.frame_ataque = 0
        self.frame_tiempo_ataque = 0
        self.frame_milisegundos_ataque = 10

        # Frames de Sprites Girando
        self.frame_girando = 0
        self.frame_tiempo_girando = 0
        self.frame_milisegundos_girando = 50

        self.tiempo_de_inicio = pg.time.get_ticks()
        
        if len(self.frames_ataque) > 0:
            self.imagen_ataque = self.frames_ataque[0]

    def movimiento(self, teclas):
        # Movimiento Jugador
        mov_x = 0
        mov_y = 0

        if teclas[pg.K_a]:
            mov_x = -1
            self.direccion = "IZQUIERDA"
            self.flip = True

        if teclas[pg.K_d]:
            mov_x = 1
            self.direccion = "DERECHA"
            self.flip = False

        if teclas[pg.K_w] and not self.en_el_aire:
            self.velocidad_y = self.velocidad_salto
            self.en_el_aire = True

        if self.en_el_aire:
            self.velocidad_y += self.gravedad
        
        mov_y = self.velocidad_y

        tiempo_actual = pg.time.get_ticks()

        # Ataque
        if teclas[pg.K_SPACE] and tiempo_actual - self.ultimo_ataque > self.cooldown:
            if not self.en_el_aire:
                if not self.atacando:
                    self.atacando = True
                    self.ultimo_ataque = tiempo_actual
                    self.tiempo_de_inicio_ataque = tiempo_actual
                    self.animar_ataque()

        # Movimiento
        self.rect.x += mov_x * self.estadisticas["Velocidad"]
        self.rect.y += mov_y
        self.hitbox.center = self.rect.center

        # Cambiar sprite del Jugador en caso de movimiento o no
        if self.en_el_aire:
            self.animar_giro()
        else:
            if mov_x != 0:
                self.animar_corriendo()
            else:
                self.imagen = self.quieto

        if self.direccion == "DERECHA":
            self.ataque_hitbox = pg.Rect(self.rect.centerx + 15, self.rect.centery - 48, 64, 64)
        if self.direccion == "IZQUIERDA":
            self.ataque_hitbox = pg.Rect(self.rect.centerx - 79, self.rect.centery - 48, 64, 64)

        if self.atacando:
            self.animar_ataque()
    
    def animar_giro(self):
        tiempo_actual = pg.time.get_ticks()
        
        if tiempo_actual - self.tiempo_de_inicio > self.frame_milisegundos_girando:  
            self.frame_girando = (self.frame_girando + 1) % len(self.frames_girando)
            self.imagen = self.frames_girando[self.frame_girando]
            self.tiempo_de_inicio = tiempo_actual